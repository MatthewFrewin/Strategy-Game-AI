import random
import subprocess
import os
from board import Board
from actor import Actor

class Game:
    def __init__(self, width=10, height=10):
        """Initialise the board and actors"""
        self.board = Board(width, height)
        self.player = Actor(2, 3, 'P')
        self.enemy = Actor(5, 5, 'E')
        self.board.place_actor(self.player.x, self.player.y, self.player.symbol)
        self.board.place_actor(self.enemy.x, self.enemy.y, self.enemy.symbol)

    def clear_screen(self):
        """Clear the screen (Windows/Mac/Linux compatible)"""
        unused_var = os.system('cls' if os.name == 'nt' else 'clear')

    def player_turn(self):
        move_map = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0), 'q': 'quit'}
        move = input("Move (WASD, Q to quit): ").lower()

        if move in move_map:
            if move == 'q':
                print("Quitting game...")
                exit(0)  # Quit game
            dx, dy = move_map[move]
            self.player.move(dx, dy, self.board)
#        else:
#            print("Invalid move! Use W (up), A (left), S (dowm), D (right).")

    def enemy_turn(self):
        """Simple enemy AI with random movement"""
        dx, dy = random.choice([(0,-1), (0,1), (-1,0), (1,0)])
        self.enemy.move(dx, dy, self.board)

    def is_game_over(self):
        """A collision between the player and the enemy means GAME OVER"""
        return self.player.x == self.enemy.x and self.player.y == self.enemy.y

    def run(self):
        """The main game loop"""
        while True:
            self.clear_screen()
            self.board.display()
            self.player_turn()
            if self.is_game_over():
                print("Game Over! The enemy caught you.")
                break

            self.enemy_turn()
            if self.is_game_over():
                print("Game Over! The enemy caught you.")
                break

# Example usage
if __name__ == "__main__":
    game = Game()
    game.run()