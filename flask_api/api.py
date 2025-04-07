import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from flask_cors import CORS
from game.game import Game

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

game_instance = Game()

@app.route("/state", methods=["GET"])
def get_game_state():
    board_data = {
        "width": game_instance.board.width,
        "height": game_instance.board.height,
        "grid": game_instance.board.grid
    }
    return jsonify(board_data)

@app.route("/move", methods=["POST"])
def move_player():
    direction = request.json.get("direction")
    if direction in ['w', 's', 'a', 'd']:
        move_map = { 'w': (0,-1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0) }
        dx, dy = move_map[direction]
        game_instance.player.move(dx, dy, game_instance.board)
    
    return jsonify({
        "grid": game_instance.board.grid,
        "width": game_instance.board.width,
        "height": game_instance.board.height
    })

@app.route("/ai", methods=["POST"])
def move_ai():
    game_instance.ai(game_instance.enemy, game_instance.player, game_instance.board)
    
    return jsonify({
        "grid": game_instance.board.grid,
        "width": game_instance.board.width,
        "height": game_instance.board.height
    })

@app.route("/reset", methods=["POST"])
def reset_game():
    global game_instance
    game_instance = Game()
    return get_game_state()

if __name__ == "__main__":
    app.run(debug=True)