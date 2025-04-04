from ai.random_ai import random_move
from ai.rule_based_ai import move_towards_player
from ai.greedy_ai import greedy_move

class AiType:
    RANDOM = "random"
    RULE_BASED = "rule_based"
    GREEDY = "greedy"

def get_ai_strategy(name):
    if name == AiType.RANDOM:
        return random_move
    elif name == AiType.RULE_BASED:
        return move_towards_player
    elif name == AiType.GREEDY:
        return greedy_move
    else:
        raise ValueError(f"Invalid strategy requested: {name}")
