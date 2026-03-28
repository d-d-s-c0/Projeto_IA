#implementaçao de um monte carlo simples
#usa as regras do popout_state

import random
from popout_state import PopOutState


#permite fazer uma jogada aleatoria
def random_move(state):
    return random.choice(state.get_valid_moves())

#obter o resultado dessa jogada
def random_playout(state, root_player):
    simulation_state = state.clone()

    while not simulation_state.is_terminal():
        move = random.choice(simulation_state.get_valid_moves())
        simulation_state.apply_move(move)

    return simulation_state.get_result(root_player)

#algoritmo de montecarlo
def monte_carlo_move(state, simulations_per_move=50):
    legal_moves = state.get_valid_moves()
    root_player = state.current_player

    best_move = None
    best_score = -1

    for move in legal_moves:
        total_score = 0

        for _ in range(simulations_per_move):
            simulation_state = state.clone()
            simulation_state.apply_move(move)

            while not simulation_state.is_terminal():
                random_move_choice = random.choice(simulation_state.get_valid_moves())
                simulation_state.apply_move(random_move_choice)

            total_score += simulation_state.get_result(root_player)

        average_score = total_score / simulations_per_move

        if average_score > best_score:
            best_score = average_score
            best_move = move

    return best_move