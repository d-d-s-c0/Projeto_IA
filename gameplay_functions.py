import time
import os
from montecarlo import monte_carlo_move

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def invalid_command(game):
    clear_terminal()
    print(game.board_to_string())
    print("Invalid command. To check command rules, use COMMANDS.")
    input("Use ENTER to PLAY AGAIN")
    return

def check_commands():
    clear_terminal()
    print('''To remove a disc from the bottom row, use R followed by the column index between 1 and 7.
For example, R5 removes the bottom disc from the 5th column.
NOTE: The disc is only removable if it belongs to the current player.
          
To insert a disc, use I followed by the column index between 1 and 7.
For example, I3 inserts a disc in the top of the 3rd column.
NOTE: The disc can only be inserted if the column is not full yet.
          
To declare a draw, use D.

To quit game, use QUIT.
''')
    input("Press ENTER to return.")
    return

def check_rules():
    clear_terminal()
    print(
'''POP OUT is a version of CONNECT 4 with some changes.

The game starts with an empty 7*6 board. Players alternate turns placing their own coloured discs into the board.
A player, in their round, can either add another disc from the top or remove a disc of one's own colour from the bottom.
The latter will drop each disc above it down one space.
The first player to connect four of their discs horizontally, vertically or diagonally wins the game.

ADDITIONAL RULES:
1. If a pop move creates four-in-rows for both players, the player who made the pop move is the winner.
2. If the board is full, the player to move decides whether he wants to make a pop move or end the game as a draw.
3. If the same state is repeated three times, either player can declare the game drawn.
''')
    input("Press ENTER to return")
    return

def CVC_play(game):
    print(game.board_to_string())
    print("Current player:", game.cur_player)
    time.sleep(0.5)
    move = monte_carlo_move(game, simulations_per_move=20)
    print("Computer plays:", move)
    time.sleep(2)
    game.apply_move(move)
    print(game.board_to_string())
    time.sleep(2)

def PVC_play(game):
    print(game.board_to_string())
    if (game.type_player == "human"): 
        print("Current player:", game.cur_player, " (human)")
        inp = input("Move: ")
        if inp == "RULES": check_rules()
        elif inp == "COMMANDS": check_commands()
        elif inp == "QUIT":
            game.terminal = True
            return
        elif inp == "D": 
            game.apply_move((inp, 0))
        elif len(inp) == 2 and inp[0] in ["I","R"]:
            col = int(inp[1])
            if (col < 0 or col > 7): invalid_command(game)
            else: game.apply_move((inp[0], col))
        else:
            invalid_command(game)
    else: 
        print("Current player:", game.cur_player, " (computer)")
        time.sleep(0.5)
        move = monte_carlo_move(game, simulations_per_move=20)
        print("Computer plays:", move)
        time.sleep(2)
        game.apply_move(move)
    print(game.board_to_string())

def PVP_play(game):
    print(game.board_to_string())
    print("Current player:", game.cur_player)
    inp = input("Move: ")
    if inp == "RULES": check_rules()
    elif inp == "COMMANDS": check_commands()
    elif inp == "QUIT": 
        game.terminal = True
        return
    elif inp == "D": 
        game.apply_move((inp, 0))
    elif len(inp) == 2 and inp[0] in ["I","R"]:
        col = int(inp[1])
        if (col < 0 or col > 7): invalid_command(game)
        else: game.apply_move((inp[0], col))
    else:
        invalid_command(game)
    print(game.board_to_string())

def win(game):
    print(game.board_to_string())
    if game.winner: print("Winner:", game.winner)
    else: print("It's a draw!")
    input("Press ENTER to return")
