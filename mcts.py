#standard version of monte carlo 
import math
import random

def other_player(player):
    return "X" if player == "O" else "O"


class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.untried_moves = state.get_valid_moves()
        self.visits = 0
        self.score = 0.0

        # Player who made the move that led to this node
        self.player_just_moved = other_player(state.cur_player)

    def is_fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, exploration=1.41):
        best_score = -float("inf")
        best_child = None

        for child in self.children:
            exploitation = child.score / child.visits
            exploration_term = exploration * math.sqrt(
                math.log(self.visits) / child.visits
            )
            uct_score = exploitation + exploration_term

            if uct_score > best_score:
                best_score = uct_score
                best_child = child

        return best_child

    def expand(self):
        move = self.untried_moves.pop()
        new_state = self.state.clone()
        new_state.apply_move(move, printing=False)

        child = MCTSNode(new_state, parent=self, move=move)
        self.children.append(child)

        return child

    def update(self, result):
        self.visits += 1
        self.score += result


def rollout(state):
    simulation_state = state.clone()

    while not simulation_state.terminal:
        move = random.choice(simulation_state.get_valid_moves())
        simulation_state.apply_move(move, printing=False)

    return simulation_state


def mcts_move(state, iterations=100):
    root = MCTSNode(state.clone())

    for _ in range(iterations):
        node = root

        # 1. Selection
        while not node.state.terminal and node.is_fully_expanded():
            node = node.best_child()

        # 2. Expansion
        if not node.state.terminal and node.untried_moves:
            node = node.expand()

        # 3. Simulation
        final_state = rollout(node.state)

        # 4. Backpropagation
        while node is not None:
            result = final_state.get_result(node.player_just_moved)
            node.update(result)
            node = node.parent

    # Choose the most visited child as the final move
    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move