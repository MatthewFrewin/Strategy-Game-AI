import random

def random_move(enemy, player, board):
    dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    enemy.move(dx, dy, board)

