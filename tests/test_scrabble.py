#test_scrabble.py
import unittest
from game.scrabble import ScrabbleGame, InvalidWordException, InvalidJokerConversion
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
        game = ScrabbleGame(2)
        word = "Facultad"
        location = (7, 7)
        orientation = "Horizontal"
        self.assertEqual(game.validate_word(word,location,orientation), True)
        
    def test_validate_word_not_in_dictionary(self):
        game = ScrabbleGame(2)
        word = "Kadabra"
        location = (0, 0)
        orientation = "Horizontal"
        
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)

    def test_validate_word_exceeds_board(self):
        game = ScrabbleGame(2)
        word = "Facultad"
        location = (14,14)
        orientation = "H"
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)
            
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
    
    def test_show_amount_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.show_amount_tiles_bag(), 29)
    
    def test_shuffle_rack(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        game.shuffle_rack()
        self.assertEqual(len(game.current_player.rack), 3)
        
    def test_clean_word_to_use(self):
        game = ScrabbleGame(2)
        word = 'Imaginación'
        self.assertEqual(game.clean_word_to_use(word), 'IMAGINACION')
    
    def test_convert_joker_fine(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('?', 0)]
        game.convert_joker('A')
        self.assertEqual(game.current_player.rack[0].letter, 'A')
        self.assertEqual(game.current_player.rack[0].value, 1)

    def test_convert_wildcard_no_wildcard(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1)]
        with self.assertRaises(InvalidJokerConversion):
            game.convert_joker('B')

    def test_input_to_int_wrong_fine(self):
        game = ScrabbleGame(2)
        string = '0'
        self.assertEqual(game.input_to_int(string), 0)

    def test_input_to_int_wrong(self):
        game = ScrabbleGame(2)
        string = 'm'
        self.assertEqual(game.input_to_int(string), None)

    def test_put_tiles_in_rack_all_players(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.put_tiles_in_rack()
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 7)
    
    def test_put_tiles_in_rack_one_player(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.next_turn()
        game.put_tiles_in_rack(1)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 1)
    
    def test_put_tiles_in_rack_few_tiles_in_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.bag_tiles.tiles = [Tile('H', 4), Tile('O', 1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O', 1), Tile('L',1), Tile('A',1)]
        game.put_tiles_in_rack(7)
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.put_tiles_in_rack(7)
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 1)

    def test_validate_orientation(self):
        game = ScrabbleGame(2)
        orientation = 'm'
        self.assertEqual(game.validate_orientation(orientation), None)
    
    def test_validate_horizontal_orientation(self):
        game = ScrabbleGame(2) 
        orientation = "Horizontal"
        result = game.validate_orientation(orientation)
        self.assertEqual(result, "Horizontal")

    def test_validate_vertical_orientation(self):
        game = ScrabbleGame(2)
        orientation = "Vertical"
        result = game.validate_orientation(orientation)
        self.assertEqual(result, "Vertical")

    def test_validate_invalid_orientation(self):
        game = ScrabbleGame(2)
        orientation = "Diagonal" 
        result = game.validate_orientation(orientation)
        self.assertIsNone(result)

    def test_put_word(self):
        game = ScrabbleGame(2)
        word = "Hola"
        location = (5, 4)
        orientation = "Horizontal"
        game.put_word(word, location, orientation)
        self.assertEqual(game.board.grid[5][4].letter.letter, "H")
        self.assertEqual(game.board.grid[5][5].letter.letter, "O")
        self.assertEqual(game.board.grid[5][6].letter.letter, "L")
        self.assertEqual(game.board.grid[5][7].letter.letter, "A")

if __name__ == "__main__":
    unittest.main()



    



