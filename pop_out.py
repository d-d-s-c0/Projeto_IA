import os
import random 
import time

def new_board(): #initializes an empty board
    b = []
    for i in range(0,6): b += [["."]*7]
    return b

def start_player(rand): #defines starting player. By default it is O, but can be randomized too.
    if (rand == False): return "O"
    else: 
        player = ["O","X"]
        return player[random.randint(0,1)]

def clear_terminal(): #clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def check(line, char):
    cur = line[0]
    count = 1
    for i in range(1, len(line)):
        if (line[i] == cur): 
            count += 1
            if (count == 4 and cur != "."):
                if (cur == char): return 1
                else: return -1
        else:
            cur = line[i]
            count = 1
    return 0

class game: #defines a new game
    def __init__(self, rand):
        self.board = new_board() #we start with an empty board
        self.board_history = {self.board_to_string(): 1} #the board history includes only the empty board, which we "visited" once
        self.cur_player = start_player(rand) #we define the starting player

    def change_player(self): #changes the player
        if (self.cur_player == "O"): self.cur_player = "X"
        else: self.cur_player = "O"
        return
    
    def print_board(self): #prints the current state of the board
        print (self.board_to_string())
        return

    def board_to_string(self): #turns the board into a string
        s = ""
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                s += self.board[row][col] + " "
            s += "\n"
        return s

    def board_is_full(self): #checks if the board is completely full
        for col in self.board[0]:
            if (col == "."): return False #means there is still an empty position in the top row
        return True #if the top row is full, then the entire board is full
    
    def check_for_win(self): #checks if there is any 4-in-row in our current board

        for row in range(0, len(self.board)): #test each row
            test = check(self.board[row], self.cur_player)
            if (test != 0): 
                self.end_game(test)
                return True

        for col in range(0, len(self.board[0])): #test each column
            cur_col = []
            for row in range(0, len(self.board)):
                cur_col += self.board[row][col]
            test = check(cur_col, self.cur_player)
            if (test != 0): 
                self.end_game(test)
                return True
        
        for row in range(0, len(self.board)): #test each diagonal
            continue #TODO
        return False
    
    def invalid_command(self): #when a command is not recognized by the game
        clear_terminal()
        self.print_board()
        print("Invalid command. To check command rules, use COMMANDS.")
        print("Use ENTER to PLAY AGAIN")
        input()
        self.make_a_move()
        return
    
    def invalid_move(self): #when a correct command corresponds to a move that cannot be played at the current state of the game
        clear_terminal()
        self.print_board()
        print("Invalid move. To check game rules, use RULES")
        print("Use ENTER to PLAY AGAIN")
        input()
        self.make_a_move()
        return
    
    def check_commands(self): #to check the command notation
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
        self.make_a_move()
        return

    def check_rules(self): #to check the rules of the game
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
        self.make_a_move()
        return
    
    def end_game(self, result): #produces an ending message to the game (result 1 means cur_player won | 0 means draw | -1 means cur_player lost)
        clear_terminal()
        self.print_board()
        if (result == 1): print("Player " + self.cur_player + " is the winner!")
        elif (result == 0): print("It's a draw!")
        else: #if the current player has lost, then change player. then, the new current player has won.
            self.change_player()
            print("Player " + self.cur_player + " is the winner!")
        print()
        print("Use RESTART or QUIT")
        while(True):
            command = input()
            if (command == "RESTART"): 
                self.restart(False)
                return
            elif (command == "QUIT"): return
            

    def remove(self, col): #removes, if possible, a disc from the last row, in position col
        try: col = int(col)
        except: self.invalid_move()
        if (col < 1 or col > 7): self.invalid_move()
        elif (self.board[len(self.board) - 1][col - 1] == self.cur_player): 
            for i in range(len(self.board) - 1, 0, -1): #shifts all discs above the removal one position down
                self.board[i][col - 1] = self.board[i - 1][col - 1]
            self.board[0][col - 1] = "."
            #check if this state has been visited before
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1 #if not, mark it as visited once
            if (self.check_for_win()): return
            self.change_player()
            self.make_a_move()
        else: self.invalid_move()
        return
    
    def insert(self, col): #inserts, if possible, a disc in the column col
        try: col = int(col)
        except: self.invalid_move()
        if (col < 1 or col > 7): self.invalid_move()
        elif (self.board[0][col - 1] == "."): #if the column col still has space...
            self.board[0][col - 1] = self.cur_player #insert disc on top of the column
            i = 0
            clear_terminal()
            self.print_board()
            while (i < 5 and self.board[i+1][col - 1] == "."): #make disc fall to the bottom
                time.sleep(0.25)
                self.board[i][col - 1] = "."
                self.board[i+1][col - 1] = self.cur_player
                i += 1
                clear_terminal()
                self.print_board()
            #check if this state has been visited before
            if (self.board_to_string() in self.board_history.keys()): self.board_history[self.board_to_string()] += 1
            else: self.board_history[self.board_to_string()] = 1 #if not, mark it as visited once
            time.sleep(0.5)
            if (self.check_for_win()): return
            self.change_player()
            self.make_a_move()
        else: self.invalid_move()
        return
    
    def draw(self): #declares a draw, if it is possible according to game rules
        if (self.board_is_full()): self.end_game(0) #if the board is full, then draw.
        elif (self.board_history[self.board_to_string()] == 3): self.end_game(0) #if we have been 3 times in the current state of the board, then draw.
        else: self.invalid_move() #else, draw is not playable yet.
        return

    def restart(self, rand): #restarts the game
        self.__init__(rand)
        self.make_a_move()
        return
        
    def make_a_move(self): #reads and interprets commands from the terminal
        clear_terminal()
        self.print_board()
        print("PLAYING NOW: " + self.cur_player)
        command = input()
        if command == "COMMANDS": self.check_commands()
        elif command == "RULES": self.check_rules()
        elif command == "RESTART": self.restart(False)
        elif command == "QUIT": return #ends this game session
        elif len(command) == 0: self.make_a_move()
        elif command[0] == "R" and len(command) == 2: self.remove(command[1])
        elif command[0] == "I" and len(command) == 2: self.insert(command[1])
        elif command == "D": self.draw()
        else: self.invalid_command()
        return
