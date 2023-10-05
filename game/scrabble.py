# scrabble.py
from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
from game.dictionary import Dictionary  # Añadir importación del diccionario

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.current_turn = 0
        self.current_player = None
        self.players: list[Player] = []
        self.dict = Dictionary()
        # Crear instancias de Player con nombres
        for i in range(players_count):
            player_name = f"Player {i+1}"
            self.players.append(Player(name=player_name, bag_tiles=self.bag_tiles))
        
    def playing(self):
        return True

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player)
            index = (index + 1) % len(self.players)
            self.current_player = self.players[index]
        self.current_turn += 1


    def validate_word(self, word, location, orientation):
        if self.dict.verify_word(word) is True:
            return self.board.validate_word_place_board(word, location, orientation)
        else:
            return False

    
    def game_over(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False
