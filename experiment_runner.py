from game.game import Game
from ai.player_bots import random_player_move

def run_experiment(ai_type, trials=100):
    wins = 0
    losses = 0
    total_turns = 0

    for _ in range(trials):
        game = Game(ai_type=ai_type, auto_mode=True, player_bot=random_player_move)
        while True:
            game.player_turn()
            if game.is_level_complete():
                wins += 1
                total_turns += game.turn_count
                break

            if game.is_game_over():
                losses += 1
                total_turns += game.turn_count
                break

            game.ai(game.enemy, game.player, game.board)
            game.turn_count += 1

    print(f"Results for {ai_type}:")
    print(f"Wins: {wins}, Losses: {losses}, Total: {trials}")
    print(f"Win Rate: {wins/trials:.2%}")
    print(f"Avg Turns/Game: {total_turns/trials:.2f}")
    print()

if __name__ == "__main__":
    for strategy in ["random", "greedy", "rule_based"]:
        run_experiment(ai_type=strategy, trials=100)
