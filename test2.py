from pop_out import Pop_Out
from mct2 import mcts_move_v2

state = Pop_Out()

while not state.terminal:
    move = mcts_move_v2(state, iterations=50)
    print("Player", state.cur_player, "plays", move)

    state.apply_move(move, printing=False)
    print(state.board_to_string())

print("Game over")
print("Winner:", state.winner)