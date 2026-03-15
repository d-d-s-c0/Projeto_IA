import os
import random 

def new_board():
    return [["."]*7]*6

def start_player(rand):
    if (rand == False): return "O"
    else: 
        player = ["O","X"]
        return player[random.randint(0,1)]

def change_player():
    if (cur_player == "O"): cur_player = "X"
    else: cur_player = "O"

def clear_terminal(): 
    os.system('cls' if os.name == 'nt' else 'clear')

board = new_board()
cur_player = start_player(False)
board_history = {board: 1}

def print_board():
    for row in board:
        s = ""
        for col in row: 
            s+= col
        print(s)

def board_is_full():
    for col in board[0]: 
        if (col == "."): return False
    return True

def invalid_command():
    print("Invalid command. To check command rules, use COMMANDS.")
    print("PLAY AGAIN")
    make_a_move()

def invalid_move():
    print("Invalid move. To check game rules, use RULES")
    print("PLAY AGAIN")
    make_a_move()

def check_commands():
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
    print("Press ENTER to return")
    input()
    make_a_move()

def check_rules():
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
    make_a_move()

def end_game(result):
    if (result == 1): print("Player " + cur_player + " is the winner!")
    elif (result == 0): print("It's a draw!")
    else:
        change_player()
        print("Player " + cur_player + " is the winner!")

def remove(col):
    try: col = int(col)
    except: invalid_move()
    if ( col < 1 or col > 7): invalid_move()
    if (board[len(board) - 1][col - 1] == cur_player): 
        for i in range(len(board) - 1, 0, -1):
            board[i][col - 1] = board[i - 1][col - 1]
        board[0][col - 1] = "."
        if (board in board_history): board_history[board] += 1
        else: board_history[board] = 1
        change_player()
        make_a_move()
    else: invalid_move()

def insert(col):
    try: col = int(col)
    except: invalid_move()
    if ( col < 1 or col > 7): invalid_move()
    if(board[0][col - 1] == "."):
        board[0][col - 1] = cur_player
        if (board in board_history): board_history[board] += 1
        else: board_history[board] = 1
        change_player()
        make_a_move()
    else: invalid_move()

def draw():
     if (board_is_full()): end_game(0)
     if (board_history[board] == 3): end_game(0)
     else: invalid_move()

def make_a_move():
    clear_terminal()
    print_board()
    print("PLAYING NOW: " + cur_player)
    command = input()
    if command == "COMMANDS": check_commands()
    if command == "RULES": check_rules()
    if command[0] == "R": remove(command[1])
    if command[0] == "I": insert(command[1])
    if command[0] == "D": draw()
    else: invalid_command()
