# MCTS Version 2 — Avoiding repeated states
import math
import random
def other_player(player):
    return "X" if player == "O" else "O"


def state_key(state):
    # A state should include both the board and the current player
    return state.board_to_string() + "TURN:" + state.cur_player


class MCTSNode:
    def __init__(self, state, parent=None, move=None, visited_states=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.score = 0.0

        self.player_just_moved = other_player(state.cur_player)

        # Store all states already visited in this path
        if visited_states is None:
            self.visited_states = {state_key(state)}
        else:
            self.visited_states = set(visited_states)
            self.visited_states.add(state_key(state))

        # Only keep moves that do not create a repeated state
        self.untried_moves = self.get_non_repeating_moves()

    def get_non_repeating_moves(self):
        non_repeating_moves = []

        for move in self.state.get_valid_moves():
            new_state = self.state.clone()
            new_state.apply_move(move, printing=False)

            if state_key(new_state) not in self.visited_states:
                non_repeating_moves.append(move)

        return non_repeating_moves

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

        child = MCTSNode(
            new_state,
            parent=self,
            move=move,
            visited_states=self.visited_states
        )

        self.children.append(child)
        return child

    def update(self, result):
        self.visits += 1
        self.score += result


def rollout(state):
    simulation_state = state.clone()
    visited_states = {state_key(simulation_state)}

    while not simulation_state.terminal:
        non_repeating_moves = []

        for move in simulation_state.get_valid_moves():
            temp = simulation_state.clone()
            temp.apply_move(move, printing=False)

            if state_key(temp) not in visited_states:
                non_repeating_moves.append(move)

        # Prefer non-repeating moves
        if non_repeating_moves:
            move = random.choice(non_repeating_moves)
        else:
            # Fallback: if all moves repeat, choose any valid move
            move = random.choice(simulation_state.get_valid_moves())

        simulation_state.apply_move(move, printing=False)
        visited_states.add(state_key(simulation_state))

    return simulation_state


def mcts_move_v2(state, iterations=100):
    root = MCTSNode(state.clone())

    for _ in range(iterations):
        node = root

        # 1. Selection
        while (
            not node.state.terminal
            and node.is_fully_expanded()
            and node.children
        ):
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

    # If no child was created, fallback to a legal move
    if not root.children:
        return random.choice(state.get_valid_moves())

    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move