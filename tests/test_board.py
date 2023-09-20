# test_board.py
import unittest
from game.board import Board
from game.tile import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

    def test_place_tile(self):
        board = Board()
        tile = Tile('A', 1)
        self.assertTrue(board.place_tile(7, 7, tile))
        self.assertFalse(board.place_tile(7, 7, tile))

    def test_validate_word(self):
        board = Board()
        tile_a = Tile('A', 1)
        tile_b = Tile('B', 2)
        tile_c = Tile('C', 3)

        board.place_tile(7, 7, tile_a)
        board.place_tile(7, 8, tile_b)
        board.place_tile(7, 9, tile_c)

        self.assertTrue(board.validate_word(7, 7, 'ABC', 'H'))
        self.assertFalse(board.validate_word(7, 7, 'ACB', 'H'))
        self.assertTrue(board.validate_word(7, 7, 'A', 'V'))
        self.assertFalse(board.validate_word(7, 7, 'AB', 'V'))
        
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        assert word_is_valid == False

    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5)  # Ubicación dentro del tablero
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)

if __name__ == '__main__':
    unittest.main()

