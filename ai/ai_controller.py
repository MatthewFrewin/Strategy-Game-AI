from ai.random_ai import random_move
from ai.rule_based_ai import move_towards_player

def get_ai_strategy(name):
    if name == "random":
        return random_move
    elif name == "rule_based":
        return move_towards_player
    else:
        raise ValueError(f"Invalid strategy requested: {name}")
