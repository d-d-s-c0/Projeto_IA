# Version 2 — Heuristic-based playout for Monte Carlo
import random 

def heuristic_playout(simulation_state):
    # Uses the heuristic-guided move instead of a random move
    return heuristic_guided_move(simulation_state)


def heuristic_guided_move(state):
    # List to store moves that do not immediately lose th in  in  e game
    safe_moves = []

    # Iterate through all possible valid moves
    for move in state.get_valid_moves():
        clone = state.clone()
        clone.apply_move(move, printing=False)

        # If this move wins immediately, play it
        if clone.terminal and clone.winner == state.cur_player:
            return move

        # Check whether the opponent can win immediately after this move
        opponent_can_win = False

        for opponent_move in clone.get_valid_moves():
            temp = clone.clone()
            temp.apply_move(opponent_move, printing=False)

            # If the opponent can win immediately after this move, mark it as unsafe
            if temp.terminal and temp.winner == clone.cur_player:
                opponent_can_win = True
                break
        #  If the opponent cannot win immediately, consider this move safe
        if not opponent_can_win:
            safe_moves.append(move)
# If there are safe moves available, choose one randomly
    if safe_moves:
        return random.choice(safe_moves)
#  If no safe moves exist, fall back to a completely random move
    return random.choice(state.get_valid_moves())
