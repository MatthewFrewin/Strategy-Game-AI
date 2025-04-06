from ai.ai_controller import AiType
from game.game import Game

if __name__ == "__main__":
    game = Game(ai_type=AiType.Q_LEARNING)
    game.run()
