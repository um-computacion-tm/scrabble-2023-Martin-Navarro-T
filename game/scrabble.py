# scrabble.py
from game.board import Board
from game.player import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = [Player(name=f"Player {i+1}") for i in range(players_count)]
        self.current_turn = 0  # Inicializar el atributo current_turn a 0
        self.current_player = None

    
    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player)
            index = (index + 1) % len(self.players)  # Circular a través de los jugadores
            self.current_player = self.players[index]
        self.current_turn += 1  # Aumentar el turno actual



