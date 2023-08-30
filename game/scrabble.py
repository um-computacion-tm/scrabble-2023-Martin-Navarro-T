# scrabble.py
from game.board import Board
from game.player import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = [Player(name=f"Player {i+1}") for i in range(players_count)]
        self.current_turn = 0
