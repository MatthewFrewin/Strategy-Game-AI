import random
from collections import defaultdict
import pickle
import os

from torchvision.datasets.utils import verify_str_arg

# Learning params..
ALPHA   = 0.1     # Learning rate
GAMMA   = 0.9     # Discount factor
EPSILON = 0.1   # Exploration rate

# actions for moving up/down/left/right
ACTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Q-Table to map state -> action -> value
Q = defaultdict(dict)

def get_state(enemy, player):
    return enemy.x, enemy.y, player.x, player.y

def choose_action(state):
    if random.random() < EPSILON or state not in Q:
        return random.choice(ACTIONS)

    return max(Q[state], key=Q[state].get, default=random.choice(ACTIONS))

def update_q(state, action, reward, next_state):
    old_q = Q[state].get(action, 0)
    future_q = max(Q[next_state].values(), default=0)
    Q[state][action] = old_q + ALPHA * (reward + GAMMA * future_q - old_q)

def load_q_table(filename="q_table.pkl"):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return defaultdict(dict, data)
    else:
        print(f"Q-table not found. Path: ({filename})")
        return defaultdict(dict)

Q_Loaded = load_q_table()

def q_learning_move(enemy, player, board):
    state = get_state(enemy, player)
    if state in Q_Loaded:
        best_action = max(Q_Loaded[state], key=Q_Loaded[state].get, default=random.choice(ACTIONS))
    else:
        best_action = random.choice(ACTIONS)
    enemy.move(*best_action, board)