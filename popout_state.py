#versão em que o computador pode jogar
#futuramente temos de fazer conexão com o play.py
#basicamente é igual ao popout.py mas sem pedidos de input

import copy

def new_board():
    return [["."] * 7 for _ in range(6)]

def check(line, char):
    count = 0
    for cell in line:
        if cell == char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


class PopOutState:
    def __init__(self, board=None, current_player="O", board_history=None, winner=None, terminal=False):
        self.board = copy.deepcopy(board) if board is not None else new_board()
        self.current_player = current_player
        self.board_history = copy.deepcopy(board_history) if board_history is not None else {}
        self.winner = winner
        self.terminal = terminal

        if not self.board_history:
            self.board_history[self.board_to_string()] = 1

    def clone(self):
        return PopOutState(
            board=self.board,
            current_player=self.current_player,
            board_history=self.board_history,
            winner=self.winner,
            terminal=self.terminal
        )

    def board_to_string(self):
        s = ""
        for row in self.board:
            s += " ".join(row) + "\n"
        return s

    def change_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def board_is_full(self):
        return all(cell != "." for cell in self.board[0])

    def get_valid_moves(self):
        moves = []

        # Insert moves
        for col in range(7):
            if self.board[0][col] == ".":
                moves.append(("I", col + 1))

        # Remove moves
        for col in range(7):
            if self.board[5][col] == self.current_player:
                moves.append(("R", col + 1))

        # Optional draw declaration
        if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3:

            moves.append(("D", None))

        return moves

    def has_four(self, player):
        # Rows
        for row in range(6):
            if check(self.board[row], player):
                return True

        # Columns
        for col in range(7):
            cur_col = []
            for row in range(6):
                cur_col.append(self.board[row][col])
            if check(cur_col, player):
                return True

        # Diagonal \
        for row in range(6 - 3):
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row + i][col + i])
                if check(diag, player):
                    return True

        # Diagonal /
        for row in range(3, 6):
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row - i][col + i])
                if check(diag, player):
                    return True

        return False

    def update_terminal_status(self, move_type):
        o_wins = self.has_four("O")
        x_wins = self.has_four("X")

        if not o_wins and not x_wins:
            return

        if move_type == "pop" and o_wins and x_wins:
            self.winner = self.current_player
            self.terminal = True
            return

        if self.current_player == "O" and o_wins:
            self.winner = "O"
            self.terminal = True
            return

        if self.current_player == "X" and x_wins:
            self.winner = "X"
            self.terminal = True
            return

        self.winner = "X" if self.current_player == "O" else "O"
        self.terminal = True

    def register_state(self):
        key = self.board_to_string()
        if key in self.board_history:
            self.board_history[key] += 1
        else:
            self.board_history[key] = 1

    def apply_insert(self, col):
        c = col - 1

        if c < 0 or c > 6:
            raise ValueError("Invalid column")

        if self.board[0][c] != ".":
            raise ValueError("Column is full")

        self.board[0][c] = self.current_player

        row = 0
        while row < 5 and self.board[row + 1][c] == ".":
            self.board[row][c] = "."
            self.board[row + 1][c] = self.current_player
            row += 1

        self.update_terminal_status("insert")
        if not self.terminal:
            self.change_player()
            self.register_state()

    def apply_remove(self, col):
        c = col - 1

        if c < 0 or c > 6:
            raise ValueError("Invalid column")

        if self.board[5][c] != self.current_player:
            raise ValueError("Bottom disc does not belong to current player")

        for row in range(5, 0, -1):
            self.board[row][c] = self.board[row - 1][c]

        self.board[0][c] = "."

        self.update_terminal_status("pop")
        if not self.terminal:
            self.change_player()
            self.register_state()

    def apply_move(self, move):
        if self.terminal:
            raise ValueError("Game is already over")

        kind, value = move

        if kind == "I":
            self.apply_insert(value)
        elif kind == "R":
            self.apply_remove(value)
        elif kind == "D":
            if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3:
                self.winner = None
                self.terminal = True
            else:
                raise ValueError("Draw declaration is not valid in this state")
        else:
            raise ValueError("Unknown move type")

    def is_terminal(self):
        return self.terminal

    def get_result(self, player):
        if not self.terminal:
            raise ValueError("Game is not over yet")

        if self.winner is None:
            return 0.5
        elif self.winner == player:
            return 1.0
        else:
            return 0.0
