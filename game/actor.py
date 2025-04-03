class Actor:
    def __init__(self, x, y, symbol):
        """Initialize an actor with (x,y) coordinates and the symbol to display."""
        self.x = x
        self.y = y
        self.symbol = symbol

    def move(self, dx, dy, board):
        """
        Moves the unit by (dx, dy) if within board bounds.
        """
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < board.width and 0 <= new_y < board.height:
            board.clear_position(self.x, self.y)  # Remove from old position
            self.x = new_x
            self.y = new_y
            board.place_actor(self.x, self.y, self.symbol)  # Place at new position
        else:
            print(f"Error: Cannot move {self.symbol} to ({new_x}, {new_y}) - Out of bounds!")

# Example usage (can be removed later)
if __name__ == "__main__":
    from board import Board  # Importing Board from board.py

    board = Board()
    player = Actor(2, 3, 'P')  # Create player unit
    enemy = Actor(5, 5, 'E')  # Create enemy unit

    board.place_actor(player.x, player.y, player.symbol)
    board.place_actor(enemy.x, enemy.y, enemy.symbol)

    board.display()

    # Move player right (+1, 0) and enemy left (-1, 0)
    player.move(1, 0, board)
    enemy.move(-1, 0, board)
    board.display()
    enemy.move(-1, 0, board)
    board.display()
    enemy.move(-1, 1, board)
    board.display()
    enemy.move(-1, 0, board)
    board.display()
    enemy.move(-1, 0, board)
    board.display()
    enemy.move(-1, 1, board)
    board.display()