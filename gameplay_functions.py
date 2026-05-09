import time
import os
import random
from mcts1 import mcts_move
from mct2 import mcts_move_v2
from mcts3 import mcts_move_v3

def clear_terminal():                                               # Function that clears the terminal, to allow for a playable text interface.
    os.system('cls' if os.name == 'nt' else 'clear')

def check(line, char):                                              # Checks a line for a 4-in-row of a specific character.
    count = 0                                                       # Variable that stores the "progression" of the 4-in-row sequence.
    for cell in line:   
        if cell == char:                                            # If the current cell is equal to that character,
            count += 1                                              # add 1 to the count.
            if count == 4: return True                              # If we reach a 4-in-row, return True.
        else: count = 0                                             # When the current cell is different, we reset our progress.
    return False                                                    # If no 4-in-rows were found, return False.

def randomize_player(start_player = None):                          # Function to choose whether the computer or the human player starts (for player vs computer mode).
    if start_player: return start_player                            # If there is a starting player previously defined, return it.
    if random.randint(0,1) == 1: return "human"                     # Otherwise, make a random decision.
    return "computer"

def invalid_move(game):                                         # Gives the human player an explanation to why the move has been rejected.
    clear_terminal()
    print(game.board_to_string())
    print("Invalid move. To check game rules, use RULES.")
    input("Use ENTER to PLAY AGAIN")

def invalid_command(game):                                          # Gives the human player an explanation to why the move has been rejected.
    clear_terminal()
    print(game.board_to_string())
    print("Invalid command. To check command rules, use COMMANDS.")
    input("Use ENTER to PLAY AGAIN")
    return

def check_commands():                                               # Gives an explanation of the commands to play the game.
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

def check_rules():                                                  # Gives an explanation about the rules of the game.
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

def CVC_play(game, algorithm, num_simulations):                                                 # Coordinates plays between two computers.
    print(game.board_to_string())
    print("Current player:", game.cur_player)
    time.sleep(0.5)
    if algorithm == "MCTS v1":
        move = mcts_move(game, iterations=num_simulations)
    elif algorithm == "MCTS v2":
        move = mcts_move_v2(game, iterations=num_simulations)
        #it is missing more MCTS versions and decision trees
    elif algorithm == "MCTS v3":
            move = mcts_move_v3(game, iterations=num_simulations)
    else: ########################################################################TODO
        move = monte_carlo_move(game, num_simulations)
    print("Computer plays:", move)
    time.sleep(1.5)
    game.apply_move(move)
    print(game.board_to_string())
    time.sleep(1.5)

def PVC_play(game, algorithm, num_simulations):                                      # Coordinates plays between a human and a computer.
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
        if algorithm == "MCTS v1":
            move = mcts_move(game, iterations=num_simulations)
        elif algorithm == "MCTS V2":
            move = mcts_move_v2(game, iterations=num_simulations)
        elif algorithm == "MCTS v3":
            move = mcts_move_v3(game, iterations=num_simulations)
        #it is missing more MCTS versions and decision trees
        else: ##################################################################TODO
            move = monte_carlo_move(game, num_simulations)
        print("Computer plays:", move)
        time.sleep(1.5)
        game.apply_move(move)
    print(game.board_to_string())

def PVP_play(game):                                                 # Coordinates plays between two human players.
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

def win(game):                                                      # Prints a final winning message adapted to each game ending.
    print(game.board_to_string())
    if game.winner: print("Winner:", game.winner)
    else: print("It's a draw!")
    input("Press ENTER to return")