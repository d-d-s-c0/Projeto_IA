from pop_out import *
import sys

while(True):
    clear_terminal()
    print("Welcome to POP OUT!")
    print()
    print("1. CHECK COMMANDS\n2. CHECK RULES\n3. PLAY\n4. EXIT")
    match(input()):
        case("1"):
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
        case("2"):
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
        case("3"):
            while(True):
                clear_terminal()
                print("Select game mode:")
                print()
                print("1. PLAYER VS PLAYER\n2. PLAYER VS COMPUTER\n3. COMPUTER VS COMPUTER\n4. RETURN TO MENU")
                match(input()):
                    case("1"):
                        clear_terminal()
                        game1 = game(False)
                        game1.make_a_move()
                    case("2"):
                        clear_terminal()
                        print("Under construction...")
                        time.sleep(2)
                    case("3"):
                        clear_terminal()
                        print("Under construction...")
                        time.sleep(2)
                    case("4"):
                        break
                    case _:
                        clear_terminal()
                        print("Invalid command! Returning to GAME SELECTION...")
                        time.sleep(2)
        case("4"):
            sys.exit("Goodbye!")
        case _: 
            clear_terminal()
            print("Invalid command! Returning to MENU...")
            time.sleep(2)
