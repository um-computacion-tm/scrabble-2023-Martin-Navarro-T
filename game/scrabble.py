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
        current_player = self.current_player
        player_letters = current_player.view_tiles()
        
        # Verificar que todas las letras de la palabra estén en las letras del jugador
        if all(letter in player_letters for letter in word):
            # Verificar si la palabra cabe en el tablero en la ubicación y orientación especificadas
            if self.board.validate_word(location[0], location[1], word, orientation):
                return True
        
        # Si no se cumple alguna de las condiciones anteriores, la palabra no es válida
        return False
'''


