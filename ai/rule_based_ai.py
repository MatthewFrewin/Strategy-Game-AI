def move_towards_player(enemy, player, board):
    """Move diagonally toward player (e.g. on both the x- AND y-axis, if needed)."""
    dx = 1 if enemy.x < player.x else (-1 if enemy.x > player.x else 0)
    dy = 1 if enemy.y < player.y else (-1 if enemy.y > player.y else 0)
    enemy.move(dx, dy, board)