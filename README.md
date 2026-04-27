# POP OUT

## Introduction
POP OUT is an adaptation of the well-known game Connect 4. The main change between these two games is that, in Pop Out, it is possible to remove discs from the bottom row, as well as inserting them. 

There are three modes:

Player VS Player allows two players to take turns in placing their disks, facing eachother in a match. 

Player VS Computer allows one player to play against the computer, trained with various search algorithms. 

Computer VS Computer shows us the results of the computer playing for both opponents in a match.

## Installation Guide
Install Python:

- Windows: install manually

    1. Download: https://www.python.org/downloads/

    2. Select "Add Python to PATH"

    3. Verify installation: python --version

- Linux: 

    1. sudo apt update

    2. sudo apt install python3

- MacOs: brew install python

## Execution Guide
The game can be initialized by executing the file play.py. There, by interacting with text menus through the terminal, all of the game's features will be accessible, as well as the rules and commands. 

## Code Architecture

The implementation is divided into several files:

- `pop_out.py`: contains the game engine and the `Pop_Out` class.

- `gameplay_functions.py`: contains terminal interface functions and game mode helpers.

- `montecarlo.py`: contains the Flat Monte Carlo agent.

- `mcts_dataset.py`: contains the initial dataset generation procedure.

- `main.py`: contains the menu and connects the playable modes.

This separation allows the game logic, interface, algorithms, and dataset generation to be developed independently.



## Credits
Diogo Sousa

Joana Antunes

Sílvia Pinto


Project for Artificial Intelligence 2025/2026
