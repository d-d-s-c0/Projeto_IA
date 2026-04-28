#Fist version: Flart monte carlo
import random

def random_playout(simulation_state):
    #Selects a random legal move from the current simulated state
    return random.choice(simulation_state.get_valid_moves())


def monte_carlo_move(state, simulations_per_move=50, playout_func=random_playout):
    #Stores the player for whom we are choosing the mode
    root_player = state.cur_player
    #Variables used to keep track of the best move found so far
    best_move = None
    best_score = -1

    #Test every legal move from the current state
    for candidate_move in state.get_valid_moves():
        total_score = 0
        #run several simulations for this candidate move
        for _ in range(simulations_per_move):
            #Clone the state so that the real game is not changed
            simulation_state = state.clone()
            #Apply the candidate move as the first move of the simulation 
            simulation_state.apply_move(candidate_move, printing=False)
 
           #Continue the game randonmly until it reaches a terminal state
            while not simulation_state.terminal:
                playout_move = playout_func(simulation_state)
                simulation_state.apply_move(playout_move, printing=False)
            #Add the result of this simulation from the root player's perspective
            total_score += simulation_state.get_result(root_player)
        #Calculate the average score
        average_score = total_score / simulations_per_move

        #If this move is better than the last one store it 
        if average_score > best_score:
            best_score = average_score
            best_move = candidate_move
   
    return best_move