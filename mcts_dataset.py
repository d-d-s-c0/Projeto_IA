from montecarlo import monte_carlo_move
import csv

def generate_dataset(game, num_games=100, filename="game_data.csv"):
    dataset = []
    for i in range(num_games):
        clone = game.clone()
        while not clone.terminal:
            best_move = monte_carlo_move(clone, simulations_per_move=100)
            dataset.append(game.features + [best_move])
            clone.apply_move(best_move)
            
    # Save to CSV for the ID3 process
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(game.feature_names + ["move"])
        writer.writerows(dataset)