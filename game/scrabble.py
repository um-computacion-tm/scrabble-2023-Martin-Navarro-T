# scrabble.py
from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
from game.dictionary import Dictionary  
import random

# Excepciones
class InvalidWordException(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.current_turn = 0
        self.current_player = None
        self.players: list[Player] = []
        self.dict = Dictionary()
        self.turn = 0
        # Crear instancias de Player con nombres
        for i in range(players_count):
            player_name = f"Player {i+1}"
            self.players.append(Player(name=player_name, bag_tiles=self.bag_tiles))
    
    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            player_turn = self.players.index(self.current_player) + 1
            self.current_player = self.players[player_turn]
        self.turn += 1

    def dict_validate_word(self, word):
        dict = Dictionary()
        return dict.verify_word(word)
    
    def clean_word_to_use(self, word):
        dict = Dictionary()
        word = dict.remove_accents(word)
        word = word.strip().upper()
        return word
    
    def validate_word(self, word, location, orientation):
        if not self.dict_validate_word(word):
            raise InvalidWordException('Su palabra no existe en el diccionario')
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidWordException('Su palabra excede el tablero')
        if not self.board.validate_word_place_board(word, location, orientation):
            #Hacer test para que corra la linea 56
            raise InvalidWordException('Su palabra no se cruza con ninguna palabra valida') 
        return True

    def game_over(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False
    
    def get_board(self):
        return self.board

    def test_get_current_player_id(self):
        game = ScrabbleGame(2)
        game.next_turn()
        self.assertEqual(game.get_current_player_id(), 1)
    def show_amount_tiles_bag(self):
        return len(self.bag_tiles.tiles)
      
    def shuffle_rack(self):
        random.shuffle(self.current_player.rack)