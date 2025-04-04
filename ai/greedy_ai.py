def greedy_move(enemy, player, board):
    """
    First, chase the player on the x-axis (e.g. horizontal).
    Once the x-position matches the player's x-position,
    begin moving towards the player on the y-axis (e.g. vertical)
    """
    dx = 0
    dy = 0

    if enemy.x != player.x:
        dx = 1 if enemy.x < player.x else -1
    elif enemy.y != player.y:
        dy = 1 if enemy.y < player.y else -1

    enemy.move(dx, dy, board)
