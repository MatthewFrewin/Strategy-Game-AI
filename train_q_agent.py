from game.game import Game
from ai.player_bots import seek_goal
from ai.q_learning_ai import get_state, choose_action, update_q, Q
import pickle

def train_q_learning_agent(episodes=1000):
    games_won = 0
    for ep in range(episodes):
        game = Game(auto_mode=True, player_bot=lambda p, b: seek_goal(p, game.level_exit, b))   ## TODO: Practice lambdas in this format for better understanding
        i = 1
        while True:
            #print(f"starting loop {i}. ")
            #game.board.display()
            i += 1
            state = get_state(game.enemy, game.player)
            action = choose_action(state)
            game.enemy.move(*action, game.board)    # What does * mean here???
            game.turn_count += 1

            # Check game outcomes
            if game.is_game_over():
                reward = 1
                next_state = get_state(game.enemy, game.player)
                update_q(state, action, reward, next_state)
                break
            elif game.is_level_complete():
                reward = -1
                next_state = get_state(game.enemy, game.player)
                update_q(state, action, reward, next_state)
                games_won += 1
                break
            else:
                reward = -0.01
                next_state = get_state(game.enemy, game.player)
                update_q(state, action, reward, next_state)
                game.player_turn()  # player bot moves

        if (ep + 1) % 100 == 0:
            print(f"Episode {ep+1} complete. Games won by player: {games_won}")

    with open("q_table.pkl", "wb") as f:
        pickle.dump(dict(Q), f)     ## TODO: Check this warning

if __name__ == "__main__":
    train_q_learning_agent(episodes=10000)