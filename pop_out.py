import copy
import time
from gameplay_functions import *

class Pop_Out():                                                    # The class which represents an instance of our Pop Out game.
    def __init__(self, board = None, cur_player = "O", board_history = None, winner = None, terminal = False):
        # An instance of the game has a board, the current player, the history of previous moves and the winner of the game (if it is finished).
        self.board = copy.deepcopy(board) if board else [["."] * 7 for _ in range(6)]
        self.cur_player = cur_player
        #We need the board history to know if we have already been in a certain state more than 3 times, in order to allow players to call a draw.
        self.board_history = copy.deepcopy(board_history) if board_history else {self.board_to_string(): 1}
        self.winner = winner
        self.terminal = terminal                                    # If the game is terminal, then no more moves can be done, and its winner (or draw) is defined.

    def clone(self):                                                # Function that clones a Pop Out game, to be used for Monte Carlo Tree Search
        return Pop_Out(board = self.board,                          # Simply creates a new game with all of the exact characteristics of the previous one
                    cur_player = self.cur_player, 
                    board_history = self.board_history, 
                    winner = self.winner, 
                    terminal = self.terminal)
    
    def board_to_string(self):                                      # Turns the board into a string, in order to be printable and readable for text interface.
        s = ""
        for row in self.board:
            s += " ".join(row) + "\n"
        return s

    def change_player(self):                                        # Switches players
        self.cur_player = "X" if self.cur_player == "O" else "O"
    
    def board_is_full(self):                                        # Checks if the board is completely full (in which case the draw is playable)
        return all(cell != "." for cell in self.board[0])
    
    def get_valid_moves(self):                                      # For the computer to select its best move, shows it what moves are available.
        moves = []
        for col in range(7):                                        
            if self.board[0][col] == ".":                           # In each column, checks if there is space for an insert at the top.
                moves.append(("I", col + 1))
            if self.board[5][col] == self.cur_player:               # Also, checks if the last cell belongs to the current player; if so, it is removable.
                moves.append(("R", col + 1))

        if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3: 
            moves.append(("D", None))                               # If the board is full, or the current state has been repeated 3 or more times, then draw is available
        return moves
    
    def has_four(self, player):                                     # Function that checks if a player has made a 4-in-row in the current game state.
        for row in range(6):                                        # Checks each row first,
            if check(self.board[row], player):
                return True

        for col in range(7):                                        # then each column,
            cur_col = []
            for row in range(6):
                cur_col.append(self.board[row][col])
            if check(cur_col, player):
                return True

        for row in range(6 - 3):                                    # then the diagonals in one direction,
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row + i][col + i])
                if check(diag, player):
                    return True

        for row in range(3, 6):                                     # finally the diagonals in the other direction.
            for col in range(7 - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row - i][col + i])
                if check(diag, player):
                    return True
        return False
    
    def update_terminal_status(self):                               # Checks if the game has ended, in its current state.
        o_wins = self.has_four("O")
        x_wins = self.has_four("X")

        if not o_wins and not x_wins: return                        # If no one has won yet, things remain the same.
        self.terminal = True                                        # If someone has won. then the game has terminated.
        if o_wins and x_wins: self.winner = self.cur_player         # If both players win, we are in the presence of a "remove", so the current player wins.
        elif o_wins: self.winner = "O"                              # Else, if only O wins, declare it the winner.
        elif x_wins: self.winner = "X"                              # Lastly, if only X wins, declare it the winner.
    
    def register_state(self):                                       # Uploads the state in the board history.
        key = self.board_to_string()
        if key in self.board_history:                               # If it has already been visited, add 1 to its number of visits.
            self.board_history[key] += 1
        else:
            self.board_history[key] = 1                             # Else, mark it as visited once.

    def insert(self, col, printing):                                # Performs an "insert" move.
        c = col - 1
        if self.board[0][c] != ".": invalid_move(self)              # If the column is full already, declare the move invalid.
        self.board[0][c] = self.cur_player                          # Else, insert current player's piece at the top...
        row = 0
        while row < 5 and self.board[row + 1][c] == ".":            # and let it fall until it lands on another piece, or the end of the board.
            if (printing):                                          # Produces the animation of the fall, which will not be seen during searching phase of MCTS.
                clear_terminal()
                print(self.board_to_string())
                time.sleep(0.125)
            self.board[row][c] = "."
            self.board[row + 1][c] = self.cur_player
            row += 1
        if (printing): clear_terminal()
        self.update_terminal_status()                               # Checks if this "insert" has produced a win...
        if not self.terminal:                                       # If not, change players and register this visit to the board.
            self.change_player()
            self.register_state()

    def remove(self, col, printing):                                # Performs a "remove" move.
        c = col - 1
        if self.board[5][c] != self.cur_player: 
            invalid_move(self)                                      # If the bottom piece does not belong to the player, declare move as invalid.
            return
        for row in range(5, 0, -1):                                 # Else, remove piece and let the ones above it fall down 1 place.
            if (printing):                                          # Produces the animation of the fall, which will not be seen during searching phase of MCTS.
                clear_terminal()
                print(self.board_to_string())
                time.sleep(0.125)
            self.board[row][c] = self.board[row - 1][c]
            self.board[row-1][c] = "."
        self.board[0][c] = "."
        if (printing): clear_terminal()
        self.update_terminal_status()                               # Checks if this "remove" has produced a win...
        if not self.terminal:                                       # If not, change players and register this visit to the board.
            self.change_player()
            self.register_state()

    def apply_move(self, move, printing = True):                    # Reads a given move and executes the corresponding action.                      
        kind, value = move[0], move[1]
        if kind == "I":                                             # Perform "insert"
            self.insert(value, printing)                            
        elif kind == "R":                                           # Perform "remove"
            self.remove(value, printing)                            
        elif kind == "D":                                           # Perform "draw"...
            if self.board_is_full() or self.board_history.get(self.board_to_string(), 0) >= 3:
                self.winner = None
                self.terminal = True                                # and end the game,
            else: invalid_move(self)                                # unless the conditions for a draw have not been met.
        
    def get_result(self, player):                                   # Returns the result of the game as a "reward" value for MCTS to evaluate the path
        if self.winner is None: return 0.5
        if self.winner == player: return 1.0
        return 0.0

class CVP_Pop_Out(Pop_Out):                                         # Extends Pop Out game by changing a couple of its functions...
    def __init__(self, board = None, cur_player = "O", board_history = None, winner = None, terminal = False, start_player = None):
        super().__init__(board, cur_player, board_history, winner, terminal)
        self.type_player = randomize_player(start_player)           # to allow for a human to play against a computer,

    def change_player(self):                                        # and to change the player type according to that.
        self.cur_player = "X" if self.cur_player == "O" else "O"
        self.type_player = "human" if self.type_player == "computer" else "computer"