from pop_out import Pop_Out, CVP_Pop_Out
from gameplay_functions import *
import sys
import time

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
                        clear_terminal()
                        game = Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVP_play(game)
                        clear_terminal()
                        win(game)
                        
                    case "2":                                       # Starts game between a human and a computer.
                        clear_terminal()
                        game = CVP_Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVC_play(game)
                        clear_terminal()
                        win(game)

                    case "3":                                       # Starts game between two computers.
                        clear_terminal()
                        game = Pop_Out()
                        while not game.terminal: 
                            clear_terminal()
                            CVC_play(game)
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