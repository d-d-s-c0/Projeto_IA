from pop_out import Pop_Out, CVP_Pop_Out
from gameplay_functions import *
from mcts1 import mcts_move        # MCTS V1 (standard)
from mct2 import mcts_move_v2      #MCTS v2 (no repetitions)
from mcts3 import mcts_move_v3
import sys
import time

def select_simulations():
    num_simulations = None
    while not num_simulations:
        clear_terminal()
        print("Introduce a number of simulations between 10 and 1000:")
        try: 
            num_simulations = int(input())
            if (num_simulations < 10 or num_simulations > 1000): 
                num_simulations = None
                clear_terminal()
                print("Number outside of selection range. Returning to SIMULATIONS SELECTION...")
                time.sleep(2)
        except:
            clear_terminal()
            print("Not a readable number. Returning to SIMULATIONS SELECTION...")
            time.sleep(2)
    return num_simulations

def select_algorithm(num = 1):
    algorithm = None
    num_simulations = None
    while not algorithm:
<<<<<<< HEAD
        clear_terminal()
        print(f"Select algorithm for COMPUTER PLAYER {num}:\n\n1. Flat Monte Carlo v1\n2. Flat MCT v2\n3. MCTS v1(standard)\n4. MCTS v2")
=======
        print(f"Select algorithm for COMPUTER PLAYER {num}:\n\n1. Flat Monte Carlo v1\n2. Flat MCT v2\n3. MCTS v1(standard)\n4. MCTS v2\n5. MCTS v3")
>>>>>>> 1c9e3f059b1363c72e159a8c3b9becbd1b9c2b25
        match(input().strip()):
            case "1": 
                algorithm = "Flat MC v1"
                num_simulations = select_simulations()
            case "2": 
                algorithm = "Flat MC v2"
                num_simulations = select_simulations()
            case "3": 
                algorithm = "MCTS v1"
                num_simulations = select_simulations()
            case "4":
                algorithm = "MCTS v2"
                num_simulations = select_simulations()
            case "5":
                algorithm = "MCTS v3"
                num_simulations = select_simulations()
            #it is missing more MCTS versions and decision trees
            case _:
                clear_terminal()
                print("Invalid command! Returning to ALGORITHM SELECTION...")
                time.sleep(2)
    return algorithm, num_simulations   

while True:
    clear_terminal()
    print("Welcome to POP OUT!\n\n1. CHECK COMMANDS\n2. CHECK RULES\n3. PLAY\n4. EXIT")
    match(input().strip()):    
        case "1": check_commands()                                  # Shows the available commands. 
        case "2": check_rules()                                     # Shows the rules of the game.
        case "3":
            while True:
                clear_terminal()
                print("Select game mode:\n\n1. PLAYER VS PLAYER\n2. PLAYER VS COMPUTER\n3. COMPUTER VS COMPUTER\n4. RETURN TO MENU")
                match(input().strip()):
                    case "1":                                       # Starts game between two human players.  
                        game = Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVP_play(game)
                        clear_terminal()
                        win(game)
                        
                    case "2":                                       # Starts game between a human and a computer.
                        algorithm, num_simulations = select_algorithm()
                        game = CVP_Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVC_play(game, algorithm, num_simulations)
                        clear_terminal()
                        win(game)

                    case "3":                                       # Starts game between two computers.
                        #algorithm = ()
                        #num_simulations = ()
                        algorithm = []
                        num_simulations = []
                        for a in [0,1]:
                            #algorithm[a], num_simulations[a] = select_algorithm(a+1)
                            alg, sims = select_algorithm(a + 1)
                            algorithm.append(alg)
                            num_simulations.append(sims)

                        game = Pop_Out()
                        a = 0
                        while not game.terminal: 
                            clear_terminal()
                            CVC_play(game, algorithm[a], num_simulations[a])
                            a = (a+1)%2
                        clear_terminal()
                        win(game)

                    case "4": break                                 # Returns to main menu.

                    case _:                                         # Handles other unrecognized commands.
                        clear_terminal()
                        print("Invalid command! Returning to GAME SELECTION...")
                        time.sleep(2)
        case "4":                                                   # Terminates execution.
            sys.exit("Goodbye!")
        case _:                                                     # Handles other unrecognized commands.
            clear_terminal()
            print("Invalid command! Returning to MENU...")
            time.sleep(2)