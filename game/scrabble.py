# scrabble.py
from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players: list[Player] = []

        # Crear instancias de Player con nombres
        for i in range(players_count):
            player_name = f"Player {i+1}"
            self.players.append(Player(name=player_name, bag_tiles=self.bag_tiles))
        
        self.current_turn = 0
        self.current_player = None

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
'''
    def validate_word(self, word, location, orientation):

        1- Validar que el jugador tiene las letras necesarias
        2- Validar que la palabra cabe en el tablero

        player_tiles = self.current_player.view_tiles()
        for letter in word:
            if letter not in player_tiles:
                return False
        
        if self.board.validate_word_inside_board(word, location, orientation):
            return True
        else:
            return False
'''


