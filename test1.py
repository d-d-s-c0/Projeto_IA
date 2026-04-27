#test the real version of monte carlo
from pop_out import Pop_Out
from mct1 import mcts_move

state = Pop_Out()

while not state.terminal:
    move = mcts_move(state, iterations=50)
    print("Player", state.cur_player, "plays", move)
    state.apply_move(move, printing=False)
    print(state.board_to_string())

print("Game over")
print("Winner:", state.winner)