import random

def random_player_move(player, board):
    dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    player.move(dx, dy, board)

def seek_goal(player, goal, board):
    dx = 1 if player.x < goal.x else -1 if player.x > goal.x else 0
    dy = 1 if player.y < goal.y else -1 if player.y > goal.y else 0

    directions = []

    # Prioritize x or y based on distance
    if abs(player.x - goal.x) > abs(player.y - goal.y):
        directions = [(dx, 0), (0, dy)]
    else:
        directions = [(0, dy), (dx, 0)]

    # Try preferred directions
    for dx, dy in directions:
        new_x = player.x + dx
        new_y = player.y + dy
        if (0 <= new_x < board.width and 0 <= new_y < board.height
                and not board.is_blocked(new_x, new_y)):
            player.move(dx, dy, board)
            return

    # Fallback: try all directions
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new_x = player.x + dx
        new_y = player.y + dy
        if (0 <= new_x < board.width and 0 <= new_y < board.height
                and not board.is_blocked(new_x, new_y)):
            player.move(dx, dy, board)
            return