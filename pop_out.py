import copy
import os
import random
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def check(line, char):
    count = 0
    for cell in line:
        if cell == char:
            count += 1
            if count == 4: return True
        else: count = 0
    return False

def randomize_player(start_player = None):
    if start_player: return start_player
    if random.randint(0,1) == 1: return "human"
    return "computer"

class Pop_Out():
    def __init__(self, board = None, cur_player = "O", board_history = None, winner = None, terminal = False):
        self.board = copy.deepcopy(board) if board else [["."] * 7 for _ in range(6)]
        self.cur_player = cur_player
        self.board_history = copy.deepcopy(board_history) if board_history else {self.board_to_string(): 1}
        self.winner = winner
        self.terminal = terminal

    def clone(self):
        return Pop_Out(board = self.board, 
                    cur_player = self.cur_player, 
                    board_history = self.board_history, 
                    winner = self.winner, 
                    terminal = self.terminal)
    
    def board_to_string(self):
        s = ""
        for row in self.board:
            s += " ".join(row) + "\n"
        return s

    def change_player(self):
        self.cur_player = "X" if self.cur_player == "O" else "O"
    
    def board_is_full(self):
        return all(cell != "." for cell in self.board[0])
    
    def get_valid_moves(self):
        moves = []
        for col in range(7):
            if self.board[0][col] == ".":
                moves.append(("I", col + 1))

        for col in range(7):
            if self.board[5][col] == self.cur_player:
                moves.append(("R", col + 1))

        if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3: 
            moves.append(("D", None))
        return moves
    
    def has_four(self, player):
        for row in range(6):
            if check(self.board[row], player):
                return True

        for col in range(7):
            cur_col = []
            for row in range(6):
                cur_col.append(self.board[row][col])
            if check(cur_col, player):
                return True

        for row in range(6 - 3):
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row + i][col + i])
                if check(diag, player):
                    return True

        for row in range(3, 6):
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row - i][col + i])
                if check(diag, player):
                    return True
        return False
    
    def update_terminal_status(self):
        o_wins = self.has_four("O")
        x_wins = self.has_four("X")

        if not o_wins and not x_wins: return
        self.terminal = True
        if o_wins and x_wins: self.winner = self.cur_player
        elif o_wins: self.winner = "O"
        elif x_wins: self.winner = "X"
    
    def register_state(self):
        key = self.board_to_string()
        if key in self.board_history:
            self.board_history[key] += 1
        else:
            self.board_history[key] = 1

    def insert(self, col, printing):
        c = col - 1
        if self.board[0][c] != ".": self.invalid_move()
        self.board[0][c] = self.cur_player
        row = 0
        while row < 5 and self.board[row + 1][c] == ".":
            if (printing):
                clear_terminal()
                print(self.board_to_string())
                time.sleep(0.25)
            self.board[row][c] = "."
            self.board[row + 1][c] = self.cur_player
            row += 1
        if (printing): clear_terminal()
        self.update_terminal_status()
        if not self.terminal:
            self.change_player()
            self.register_state()

    def remove(self, col, printing):
        c = col - 1
        if self.board[5][c] != self.cur_player: 
            self.invalid_move()
            return
        for row in range(5, 0, -1):
            if (printing):
                clear_terminal()
                print(self.board_to_string())
                time.sleep(0.25)
            self.board[row][c] = self.board[row - 1][c]
        self.board[0][c] = "."
        if (printing): clear_terminal()
        self.update_terminal_status()
        if not self.terminal:
            self.change_player()
            self.register_state()

    def apply_move(self, move, printing = True):
        if self.terminal: self.invalid_game()
        kind, value = move[0], move[1]
        if kind == "I":
            self.insert(value, printing)
        elif kind == "R":
            self.remove(value, printing)
        elif kind == "D":
            if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3:
                self.winner = None
                self.terminal = True
            else: self.invalid_move()

    def invalid_move(self):
        clear_terminal()
        print(self.board_to_string())
        print("Invalid move. To check game rules, use RULES")
        input("Use ENTER to PLAY AGAIN")

    def invalid_game(self): raise ValueError("Game state does not allow this operation.")
        
    def get_result(self, player):
        if not self.terminal: self.invalid_game()
        if self.winner is None: return 0.5
        if self.winner == player: return 1.0
        return 0.0

class CVP_Pop_Out(Pop_Out):
    def __init__(self, board = None, cur_player = "O", board_history = None, winner = None, terminal = False, start_player = None):
        super().__init__(board, cur_player, board_history, winner, terminal)
        self.type_player = randomize_player(start_player)

    def change_player(self):
        self.cur_player = "X" if self.cur_player == "O" else "O"
        self.type_player = "human" if self.type_player == "computer" else "computer"