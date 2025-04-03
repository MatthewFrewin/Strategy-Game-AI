class Board:
    EmptyCharacter = '.'

    def __init__(self, width=10, height=10):
        """Initialise a game board with the given width/height"""
        self.width = width
        self.height = height
        self.grid = [[Board.EmptyCharacter for _ in range(width)] for _ in range(height)]

    def display(self):
        """Display the game board (ASCII)"""
        print("\n".join(" ".join(row) for row in self.grid))
        print()

    def place_actor(self, x, y, symbol):
        """Position an object/item/character on the board at the given (x,y) coordinates"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = symbol
        else:
            print(f"Error - out of bounds (Board.place_unit(x: {x}, y: {y}, symbol: {symbol}")

    def clear_position(self, x, y):
        """Remove an object from the board at the given position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = Board.EmptyCharacter


# Example usage:
if __name__ == "__main__":
    board = Board()
    board.place_actor(2, 3, 'P')  # Example: Place player at (2,3)
    board.place_actor(5, 5, 'E')  # Example: Place enemy at (5,5)

    board.place_actor(7, 1, 'E')  # Example: Place enemy at (5,5)
    board.display()