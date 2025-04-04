import random
from collections import defaultdict

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