import os
import random 
import time

def new_board():
    return [["."]*7]*6

def start_player(rand):
    if (rand == False): return "O"
    else: 
        player = ["O","X"]
        return player[random.randint(0,1)]

def clear_terminal(): 
    os.system('cls' if os.name == 'nt' else 'clear')

class game:
    def __init__(self, rand):
        self.board = new_board()
        self.board_history = {self.board_to_string(): 1}
        self.cur_player = start_player(rand)

    def change_player(self):
        if (self.cur_player == "O"): self.cur_player = "X"
        else: self.cur_player = "O"
    
    def print_board(self):
        print (self.board_to_string())

    def board_to_string(self):
        s = ""
        for row in self.board:
            s2 = ""
            for col in row:
                s2+= col
            s+= s2 + "\n"
        return s

    def board_is_full(self):
        for col in self.board[0]: 
            if (col == "."): return False
        return True
    
    def invalid_command(self):
        clear_terminal()
        self.print_board()
        print("Invalid command. To check command rules, use COMMANDS.")
        print("Use ENTER to PLAY AGAIN")
        input()
        self.make_a_move()
    
    def invalid_move(self):
        clear_terminal()
        self.print_board()
        print("Invalid move. To check game rules, use RULES")
        print("Use ENTER to PLAY AGAIN")
        input()
        self.make_a_move()
    
    def check_commands(self):
        input()
        clear_terminal()
        print("To remove a disc from the bottom row, use R followed by the column index between 1 and 7.")
        print("For example, R5 removes the bottom disc from the 5th column.")
        print("NOTE: The disc is only removable if it belongs to the current player.")
        print()
        print("To insert a disc, use I followed by the column index between 1 and 7.")
        print("For example, I3 inserts a disc in the top of the 3rd column.")
        print("NOTE: The disc can only be inserted if the column is not full yet.")
        print()
        print("To declare a DRAW, use D.")
        print()
        print("To restart game, use RESTART")
        print()
        print("Press ENTER to return")
        input()
        self.make_a_move()

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
        time.sleep(1)
        input()
        self.make_a_move()
    
    def end_game(self, result):
        if (result == 1): print("Player " + self.cur_player + " is the winner!")
        elif (result == 0): print("It's a draw!")
        else:
            self.change_player()
            print("Player " + self.cur_player + " is the winner!")
    
    def remove(self, col):
        try: col = int(col)
        except: self.invalid_move()
        if (col < 1 or col > 7): self.invalid_move()
        if (self.board[len(self.board) - 1][col - 1] == self.cur_player): 
            for i in range(len(self.board) - 1, 0, -1):
                self.board[i][col - 1] = self.board[i - 1][col - 1]
            self.board[0][col - 1] = "."
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1
            self.change_player()
            self.make_a_move()
        else: self.invalid_move()
    
    def insert(self, col):
        try: col = int(col)
        except: self.invalid_move()
        if (col < 1 or col > 7): self.invalid_move()
        if(self.board[0][col - 1] == "."):
            self.board[0][col - 1] = self.cur_player
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1
            self.change_player()
            self.make_a_move()
        else: self.invalid_move()
    
    def draw(self):
        if (self.board_is_full()): self.end_game(0)
        if (self.board_history[self.board_to_string()] == 3): self.end_game(0)
        else: self.invalid_move()

    def restart(self, rand):
        self.__init__(rand)
    
    def make_a_move(self):
        clear_terminal()
        self.print_board()
        print("PLAYING NOW: " + self.cur_player)
        command = input()
        if command == "COMMANDS": self.check_commands()
        elif command == "RULES": self.check_rules()
        elif command == "RESTART": self.restart(False)
        elif command[0] == "R" and len(command) == 2: self.remove(command[1])
        elif command[0] == "I" and len(command) == 2: self.insert(command[1])
        elif command[0] == "D" and len(command) == 1: self.draw()
        else: self.invalid_command()

