import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile
from game.board import Board
from game.cell import Cell
from game.player import Player
from game.dictionary import Dictionary

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertEqual(scrabble_game.current_turn, 0)

    def test_playing(self):
        game = ScrabbleGame(players_count=2)
        self.assertTrue(game.playing())

    def test_next_turn(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.turn, 0)
        game.next_turn()
        self.assertEqual(game.turn, 1)

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
        
    def test_validate_word(self):
        scrabble_game = ScrabbleGame(2)
        word = "Facultad"
        location = (7, 7)
        orientation = "Horizontal"
        self.assertEqual(scrabble_game.validate_word(word,location,orientation), True)
        
    def test_validate_word_false(self):
        scrabble_game = ScrabbleGame(2)
        word = "Kadabra"
        location = (0,0)
        orientation = "Horizontal"
        self.assertEqual(scrabble_game.validate_word(word, location, orientation), False)
    
    def test_validate_word_invalid_word(self):
        scrabble_game = ScrabbleGame(2)
        word = "Imvalid"  # Una palabra que sabemos que no está en el diccionario
        location = (7, 7)
        orientation = "Horizontal"
        
        result = scrabble_game.validate_word(word, location, orientation)
        
        self.assertFalse(result)

    def test_game_over_true(self):
        game = ScrabbleGame(players_count=2)
        game.bag_tiles.tiles = []  # Vacía la bolsa de fichas

        is_game_over = game.game_over()

        self.assertTrue(is_game_over)

    def test_game_over_false(self):
        game = ScrabbleGame(players_count=2)
        game.bag_tiles.tiles = [Tile('A', 1)]  # Agrega una ficha a la bolsa

        is_game_over = game.game_over()

        self.assertFalse(is_game_over)

if __name__ == "__main__":
    unittest.main()



    



