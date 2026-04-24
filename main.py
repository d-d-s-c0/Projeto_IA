from pop_out import Pop_Out, CVP_Pop_Out
from gameplay_functions import *
import sys
import time

while True:
    clear_terminal()
    print("Welcome to POP OUT!")
    print()
    print("1. CHECK COMMANDS\n2. CHECK RULES\n3. PLAY\n4. EXIT")
    match(input().strip()):
        case "1": check_commands()
        case "2": check_rules()
        case "3":
            while True:
                clear_terminal()
                print("Select game mode:")
                print()
                print("1. PLAYER VS PLAYER\n2. PLAYER VS COMPUTER\n3. COMPUTER VS COMPUTER\n4. RETURN TO MENU")
                match(input().strip()):
                    case "1":
                        clear_terminal()
                        game = Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVP_play(game)
                        clear_terminal()
                        win(game)
                        
                    case "2":
                        clear_terminal()
                        game = CVP_Pop_Out()
                        while not game.terminal:
                            clear_terminal()
                            PVC_play(game)
                        clear_terminal()
                        win(game)

                    case "3":
                        clear_terminal()
                        game = Pop_Out()
                        while not game.terminal: 
                            clear_terminal()
                            CVC_play(game)
                        clear_terminal()
                        win(game)

                    case "4": break

                    case _:
                        clear_terminal()
                        print("Invalid command! Returning to GAME SELECTION...")
                        time.sleep(2)
        case "4":
            sys.exit("Goodbye!")
        case _:
            clear_terminal()
            print("Invalid command! Returning to MENU...")
            time.sleep(2)