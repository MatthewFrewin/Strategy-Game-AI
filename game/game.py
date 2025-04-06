import random
import os
from game.board import Board
from game.actor import Actor
from ai.ai_controller import get_ai_strategy

class Game:
    PLAYER_SYMBOL = 'P'
    ENEMY_SYMBOL = 'E'
    WIN_SYMBOL = 'W'

    def __init__(self, width=10, height=10, ai_type="random", auto_mode=False, player_bot=None):
        """Initialise the board and actors"""
        self.board = Board(width, height)
        self.board.load_from_file("levels/level3.txt")  # Load level

        px, py = self.board.find_symbol(Game.PLAYER_SYMBOL)
        ex, ey = self.board.find_symbol(Game.ENEMY_SYMBOL)
        wx, wy = self.board.find_symbol(Game.WIN_SYMBOL)

        self.player = Actor(px,py, Game.PLAYER_SYMBOL)
        self.enemy = Actor(ex, ey, Game.ENEMY_SYMBOL)
        self.level_exit = Actor(wx, wy, Game.WIN_SYMBOL)

        self.board.place_actor(self.player.x, self.player.y, self.player.symbol)
        self.board.place_actor(self.enemy.x, self.enemy.y, self.enemy.symbol)
        self.board.place_actor(self.level_exit.x, self.level_exit.y, self.level_exit.symbol)

        self.ai = get_ai_strategy(ai_type)
        self.turn_count = 0

        self.auto_mode = auto_mode
        self.player_bot = player_bot

    def clear_screen(self):
        """Clear the screen (Windows/Mac/Linux compatible)"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def player_turn(self):
        if self.auto_mode and self.player_bot:
            self.player_bot(self.player, self.board)
        else:
            move_map = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0), 'q': 'quit'}
            move = input("Move (WASD, Q to quit): ").lower()

            if move in move_map:
                if move == 'q':
                    print("Quitting game...")
                    exit(0)  # Quit game
                dx, dy = move_map[move]
                self.player.move(dx, dy, self.board)

    def is_game_over(self):
        """A collision between the player and the enemy means GAME OVER"""
        return self.player.x == self.enemy.x and self.player.y == self.enemy.y

    def is_level_complete(self):
        """Check if the player has won by reaching the level exit"""
        return self.player.x == self.level_exit.x and self.player.y == self.level_exit.y

    def run(self):
        """The main game loop"""
        while True:
            self.clear_screen()
            self.board.display()
            self.player_turn()
            if self.is_level_complete():
                print("Congratulations, you won!")
                break

            if self.is_game_over():
                print("Game Over! The enemy caught you.")
                break

            #self.enemy_turn()
            #move_towards_player(self.enemy, self.player, self.board)
            self.ai(self.enemy, self.player, self.board)

            self.turn_count += 1
            if self.is_game_over():
                print("Game Over! The enemy caught you.")
                break

# Example usage
if __name__ == "__main__":
    game = Game()
    game.run()