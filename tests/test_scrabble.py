import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile
from unittest.mock import patch

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertEqual(scrabble_game.current_turn, 0)

    def test_playing(self):
        game = ScrabbleGame(players_count=2)
        self.assertTrue(game.playing())

    def test_next_turn(self):
        game = ScrabbleGame(players_count=3)
        current_turn = game.current_turn
        game.next_turn()
        self.assertEqual(game.current_turn, current_turn + 1)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[1].name)

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)

if __name__ == '__main__':
    unittest.main()
####################################################################################################
'''
    def test_validate_word_valid(self):
        # Crear un juego de Scrabble con un jugador
        game = ScrabbleGame(players_count=1)
        # Establecer las letras del jugador para este caso de prueba
        game.current_player.tiles = ['A', 'B', 'C', 'D', 'E']

        # Configurar el tablero con algunas fichas previas
        game.board.grid[7][7].add_letter(Tile('F', 1))
        game.board.grid[7][8].add_letter(Tile('I', 1))
        
        # La palabra "CAB" debería ser válida en la ubicación (7, 6) con orientación 'H'
        result = game.validate_word('CAB', (7, 6), 'H')
        self.assertTrue(result)


    def test_validate_word_invalid_not_enough_letters(self):
        game = ScrabbleGame(players_count=1)
        game.current_player.tiles = ['A', 'B', 'D', 'E']
        
        # La palabra "CAB" no tiene suficiente letra 'C' en las letras del jugador
        result = game.validate_word('CAB', (7, 6), 'H')
        self.assertFalse(result)

    def test_validate_word_invalid_word_does_not_fit(self):
        game = ScrabbleGame(players_count=1)
        game.current_player.tiles = ['A', 'B', 'C', 'D', 'E']
        
        # La palabra "CAB" no cabe en el tablero en la ubicación (7, 7) con orientación 'V'
        result = game.validate_word('CAB', (7, 7), 'V')
        self.assertFalse(result)

    def test_validate_word_invalid_word_not_in_dictionary(self):
        game = ScrabbleGame(players_count=1)
        game.current_player.tiles = ['X', 'Y', 'Z']
        
        # La palabra "XYZ" no está en el diccionario
        result = game.validate_word('XYZ', (7, 6), 'H')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
'''