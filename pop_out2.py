import os
import random
import time

def new_board():
    b = []
    for i in range(0,6): b += [["."]*7]
    return b

def start_player(rand):
    if (rand == False): return "O"
    else: 
        player = ["O","X"]
        return player[random.randint(0,1)]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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

class game:
    def __init__(self, rand):
        self.board = new_board()
        self.board_history = {self.board_to_string(): 1}
        self.cur_player = start_player(rand)
        self.running = True

    def change_player(self):
        if (self.cur_player == "O"): self.cur_player = "X"
        else: self.cur_player = "O"
        return
    
    def print_board(self):
        print(self.board_to_string())
        return

    def board_to_string(self):
        s = ""
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                s += self.board[row][col] + " "
            s += "\n"
        return s

    def board_is_full(self):
        for col in self.board[0]:
            if (col == "."): return False
        return True
    
    def check_for_win(self, move_type="insert"):
        o_wins = False
        x_wins = False

        for row in range(len(self.board)):
            if check(self.board[row], "O"): o_wins = True
            if check(self.board[row], "X"): x_wins = True

        for col in range(len(self.board[0])):
            cur_col = []
            for row in range(len(self.board)):
                cur_col.append(self.board[row][col])
            if check(cur_col, "O"): o_wins = True
            if check(cur_col, "X"): x_wins = True

        for row in range(len(self.board) - 3):
            for col in range(len(self.board[0]) - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row + i][col + i])
                if check(diag, "O"): o_wins = True
                if check(diag, "X"): x_wins = True

        for row in range(3, len(self.board)):
            for col in range(len(self.board[0]) - 3):
                diag = []
                for i in range(4):
                    diag.append(self.board[row - i][col + i])
                if check(diag, "O"): o_wins = True
                if check(diag, "X"): x_wins = True

        if not o_wins and not x_wins:
            return False

        if move_type == "pop" and o_wins and x_wins:
            self.end_game(1)
            return True

        if self.cur_player == "O" and o_wins:
            self.end_game(1)
            return True

        if self.cur_player == "X" and x_wins:
            self.end_game(1)
            return True

        self.end_game(-1)
        return True

    def invalid_command(self):
        clear_terminal()
        self.print_board()
        print("Invalid command. To check command rules, use COMMANDS.")
        print("Use ENTER to PLAY AGAIN")
        input()
        return
    
    def invalid_move(self):
        clear_terminal()
        self.print_board()
        print("Invalid move. To check game rules, use RULES")
        print("Use ENTER to PLAY AGAIN")
        input()
        return

    def check_commands(self):
        clear_terminal()
        print("To remove a disc from the bottom row, use R followed by the column index between 1 and 7.")
        print("For example, R5 removes the bottom disc from the 5th column.")
        print("NOTE: The disc is only removable if it belongs to the current player.")
        print()
        print("To insert a disc, use I followed by the column index between 1 and 7.")
        print("For example, I3 inserts a disc in the top of the 3rd column.")
        print("NOTE: The disc can only be inserted if the column is not full yet.")
        print()
        print("To declare a draw, use D.")
        print()
        print("To restart game, use RESTART")
        print()
        print("To end game and return to menu, use QUIT")
        print()
        print("Press ENTER to return")
        input()
        return

    def check_rules(self):
        clear_terminal()
        print("POP OUT is a version of CONNECT 4 with some changes.")
        print()
        print("The game starts with an empty 7*6 board. Players alternate turns placing their own coloured discs into the board.")
        print("A player, in their round, can either add another disc from the top or remove a disc of one's own colour from the bottom.")
        print("The latter will drop each disc above it down one space.")
        print("The first player to connect four of their discs horizontally, vertically or diagonally wins the game.")
        print()
        print("ADDITIONAL RULES:")
        print("1. If a pop move creates four-in-rows for both players, the player who made the pop move is the winner.")
        print("2. If the board is full, the player to move decides whether he wants to make a pop move or end the game as a draw.")
        print("3. If the same state is repeated three times, either player can declare the game drawn.")
        print()
        print("Press ENTER to return")
        input()
        return
    
    def end_game(self, result):
        clear_terminal()
        self.print_board()
        if (result == 1): print("Player " + self.cur_player + " is the winner!")
        elif (result == 0): print("It's a draw!")
        else:
            self.change_player()
            print("Player " + self.cur_player + " is the winner!")
        print()
        print("Use RESTART or QUIT")
        while(True):
            command = input()
            if (command == "RESTART"): 
                self.restart(False)
                return
            elif (command == "QUIT"):
                self.running = False
                return

    def remove(self, col):
        try: col = int(col)
        except:
            self.invalid_move()
            return                          # ← correção
        if (col < 1 or col > 7):
            self.invalid_move()
            return                          # ← correção
        elif (self.board[len(self.board) - 1][col - 1] == self.cur_player): 
            for i in range(len(self.board) - 1, 0, -1):
                self.board[i][col - 1] = self.board[i - 1][col - 1]
            self.board[0][col - 1] = "."
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1
            if (self.check_for_win("pop")): return
            self.change_player()
            return
        else: self.invalid_move()
        return
    
    def insert(self, col):
        try: col = int(col)
        except:
            self.invalid_move()
            return                          # ← correção
        if (col < 1 or col > 7):
            self.invalid_move()
            return                          # ← correção
        elif (self.board[0][col - 1] == "."):
            self.board[0][col - 1] = self.cur_player
            i = 0
            clear_terminal()
            self.print_board()
            while (i < 5 and self.board[i+1][col - 1] == "."):
                time.sleep(0.25)
                self.board[i][col - 1] = "."
                self.board[i+1][col - 1] = self.cur_player
                i += 1
                clear_terminal()
                self.print_board()
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1
            time.sleep(0.5)
            if (self.check_for_win("insert")): return
            self.change_player()
            return
        else: self.invalid_move()
        return
    
    def draw(self):
        if self.board_is_full():
            self.end_game(0)
        elif self.board_history[self.board_to_string()] >= 3:
            self.end_game(0)
        else:
            self.invalid_move()
        return

    def restart(self, rand):
        self.__init__(rand)
        self.make_a_move()
        return
        
    def make_a_move(self):
        self.running = True

        while self.running:
            clear_terminal()
            self.print_board()
            print("PLAYING NOW: " + self.cur_player)

            command = input().strip()

            if command.upper() == "COMMANDS":
                self.check_commands()
                continue
            elif command.upper() == "RULES":
                self.check_rules()
                continue
            elif command.upper() == "RESTART":
                self.restart(False)
                return
            elif command.upper() == "QUIT":
                self.running = False
                return
            elif len(command) == 0:
                continue
            elif (command[0].upper() == "R") and len(command) == 2:
                self.remove(command[1])
            elif (command[0].upper() == "I") and len(command) == 2:
                self.insert(command[1])
            elif command.upper() == "D":
                self.draw()
            else:
                self.invalid_command()