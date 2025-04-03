def move_towards_player(enemy, player, board):
    """Move the enemy directly towards the player"""
    dx = 0 #1 if enemy.x < player.x else -1
    dy = 0 #1 if enemy.y < player.y else -1

    if enemy.x != player.x:
        dx = 1 if enemy.x < player.x else -1
    elif enemy.y != player.y:
        dy = 1 if enemy.y < player.y else -1

    enemy.move(dx, dy, board)
