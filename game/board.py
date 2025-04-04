class Board:
    EMPTY_SYMBOL = '.'
    WALL_SYMBOL = 'X'

    def __init__(self, width=10, height=10):
        """Initialise a game board with the given width/height"""
        self.width = width
        self.height = height
        self.grid = [[Board.EMPTY_SYMBOL for _ in range(width)] for _ in range(height)]

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
            self.grid[y][x] = Board.EMPTY_SYMBOL

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            self.height = len(lines)
            self.width = max(len(line) for line in lines)

            # Allows for levels with irregular shapes (needs work, as it will load the wrong shap due to ljust()
            # self.grid = [list(line.ljust(self.width, '.')) for line in lines]

            # Only works for rectangular levels:
            # self.grid = [[char for _, char in enumerate(row)] for y, row in enumerate(lines)]

            # Safer level loading, allows any shape:
            self.grid = [[Board.EMPTY_SYMBOL for _ in range(self.width)] for _ in range(self.height)]

            for y, row in enumerate(lines):
                for x, char in enumerate(row):
                        self.grid[y][x] = char

    def find_symbol(self, symbol):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if char == symbol:
                    return x, y

    def is_blocked(self, x,y):
        return self.grid[y][x] == Board.WALL_SYMBOL

# Example usage:
if __name__ == "__main__":
    from game.game import Game

    board = Board()
    board.place_actor(2, 3, Game.PLAYER_SYMBOL)  # Example: Place player at (2,3)
    board.place_actor(5, 5, Game.ENEMY_SYMBOL)  # Example: Place enemy at (5,5)

    board.display()