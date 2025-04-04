import random

def random_player_move(player, board):
    dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    player.move(dx, dy, board)
