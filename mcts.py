#Standard version of Monte Carlo Tree Search (MCTS)

import math
import random


# Helper function: switches between players
def other_player(player):
    return "X" if player == "O" else "O"


class MCTSNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state   # Current game state at this node
        self.parent = parent  # Parent node in the tree
        self.move = move       # Move that led to this state
        self.children = []     # List of child nodes
        self.untried_moves = state.get_valid_moves()  # Moves not yet explored
        self.visits = 0 # Number of times node was visited
        self.score = 0.0   # Total reward accumulated

        # Player who made the move that led to this node
        self.player_just_moved = other_player(state.cur_player)

 # Check if all possible moves from this node have been explored
    def is_fully_expanded(self):
        return len(self.untried_moves) == 0
    
 # Select the best child using UCT (Upper Confidence Bound applied to Trees)
    def best_child(self, exploration=1.41):
        best_score = -float("inf")
        best_child = None

        for child in self.children:
            # Exploitation: how good this node has been so far
            exploitation = child.score / child.visits
            # Exploration: encourages trying less-visited nodes
            exploration_term = exploration * math.sqrt(
                math.log(self.visits) / child.visits
            )

             # UCT formula balances exploration vs exploitation
            uct_score = exploitation + exploration_term

            if uct_score > best_score:
                best_score = uct_score
                best_child = child

        return best_child

   # Expand the tree by trying one untried move
    def expand(self):
        move = self.untried_moves.pop()  # Take one unexplored move
        new_state = self.state.clone()  # Clone current state and apply the move
        new_state.apply_move(move, printing=False)

       # Create new child node
        child = MCTSNode(new_state, parent=self, move=move)
        self.children.append(child)

        return child

     # Update node statistics after a simulation
    def update(self, result):
        self.visits += 1 # Increment visit count
        self.score += result # Add simulation result (win/loss/draw score)

# Perform a random simulation (playout) from a given state
def rollout(state):
    simulation_state = state.clone()
     # Play randomly until the game ends
    while not simulation_state.terminal:
        move = random.choice(simulation_state.get_valid_moves())
        simulation_state.apply_move(move, printing=False)

    return simulation_state

# Main MCTS function: returns the best move from the current state
def mcts_move(state, iterations=100):
    root = MCTSNode(state.clone())

    for _ in range(iterations):
        node = root

        # 1. Selection
           # Traverse the tree by selecting best children until we reach a leaf
        while not node.state.terminal and node.is_fully_expanded():
            node = node.best_child()

        # 2. Expansion
        # If we haven't reached a terminal state, expand one new child
        if not node.state.terminal and node.untried_moves:
            node = node.expand()

        # 3. Simulation
        # Play randomly from this node until the game ends
        final_state = rollout(node.state)

        # 4. Backpropagation
        # Propagate the result back up the tree
        while node is not None:
            # Get result from perspective of the player who just moved
            result = final_state.get_result(node.player_just_moved)
            node.update(result)
            node = node.parent # Move up the tree

    # Choose the most visited child as the final move
    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move