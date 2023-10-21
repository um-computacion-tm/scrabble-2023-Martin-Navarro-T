import unittest
from unittest.mock import Mock, patch
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile
from game.board import Board
from game.cell import Cell

class MockBoard:
    def __init__(self):
        self.grid = [[MockCell() for _ in range(15)] for _ in range(15)]

class MockCell:
    def __init__(self):
        self.letter = None
        self.multiplier = 1
        self.multiplier_type = ''

    def add_letter(self, letter):
        self.letter = letter

    def calculate_value(self):
        return self.letter.value if self.letter is not None else 0

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(name='Player 1')
        self.assertEqual(len(player_1.tiles), 0)
        self.assertEqual(player_1.score, 0)
        self.assertFalse(player_1.is_current_turn)
        self.assertEqual(player_1.name, 'Player 1')

    def test_draw_tiles(self):
        player = Player(name='Player 1')
        bag_tiles = BagTiles()

        player.draw_tiles(bag_tiles, 5)
        self.assertEqual(len(player.tiles), 5)

    def test_exchange_tiles(self):
        bag1 = BagTiles()
        player = Player(name='Player 1')
        player.rack = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        player.exchange_tiles(2, bag1)
        self.assertEqual(len(player.rack), 3)
        self.assertEqual(len(bag1.tiles), 29)

    def test_view_tiles(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        tiles = player.view_tiles()
        self.assertEqual(tiles, player.tiles)

    def test_view_score(self):
        player = Player(name='Player 1')
        player.score = 15
        score = player.view_score()
        self.assertEqual(score, player.score)

    def test_start_end_turn(self):
        player = Player(name='Player 1')

        player.start_turn()
        self.assertTrue(player.is_current_turn)

        player.end_turn()
        self.assertFalse(player.is_current_turn)

    def test_pass_turn(self):
        player = Player("Player1")
        self.assertFalse(player.is_current_turn)
        player.start_turn()
        self.assertTrue(player.is_current_turn)
        player.pass_turn()
        self.assertFalse(player.is_current_turn)

    def test_check_tile_in_hand(self):
        player = Player("Player1")
        player.tiles = ['A', 'B', 'C']
        self.assertTrue(player.check_tile_in_hand('A'))
        self.assertTrue(player.check_tile_in_hand('B'))
        self.assertTrue(player.check_tile_in_hand('C'))
        self.assertFalse(player.check_tile_in_hand('D'))
        self.assertFalse(player.check_tile_in_hand('Z'))

    def test_get_hand_size(self):
        player = Player("Player1")
        player.tiles = ['A', 'B', 'C']
        self.assertEqual(player.get_hand_size(), 3)

    def test_get_score_no_played_cells(self):
        player = Player('Charlie')
        player.board = Mock()
        player.board.played_cells = []
        self.assertEqual(player.get_score(), 0)

    def test_get_score_with_played_cells(self):
        player = Player('Charlie')
        player.board = Mock()
        mock_cell_1 = MockCell(3)
        mock_cell_2 = MockCell(2)
        player.board.played_cells = [mock_cell_1, mock_cell_2]
        self.assertEqual(player.get_score(), 5)

    def test_validate_rack_true(self):
        player_1 = Player(name='Player 1')
        tiles = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1)]
        player_1.rack = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1), Tile("Z", 1), Tile("Z", 1), Tile("Z", 1)]
        is_valid = player_1.has_letters(tiles)
        self.assertTrue(is_valid)

    def test_validate_rack_false(self):
        player_1 = Player(name='Player 1')
        tiles = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1)]
        player_1.rack = [Tile("H", 1), Tile("O", 1), Tile("E", 1), Tile("A", 1), Tile("Z", 1), Tile("Z", 1), Tile("Z", 1)]
        is_valid = player_1.has_letters(tiles)
        self.assertFalse(is_valid)

    def test_set_tiles(self):
        player = Player(name="Player 1", bag_tiles=None)
        tiles = ["a", "b", "c", "d", "e"]
        player.set_tiles(tiles)
        self.assertEqual(player.get_tiles(), tiles)

    def test_get_tiles(self):
        player = Player(name="Player 1", bag_tiles=None)
        tiles = ["a", "b", "c", "d", "e"]
        player.set_tiles(tiles)
        self.assertEqual(player.get_tiles(), tiles)
    
    def test_has_joker_true(self):
        player = Player(name="Player 1")
        player.rack = [Tile('A', 1), Tile('?', 0)]
        self.assertEqual(player.has_joker(), True)

    def test_has_joker_false(self):
        player = Player(name="Player 1")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.has_joker(), False)
    
    def test_find_joker(self):
        player = Player(name="Player 1")
        player.rack = [Tile('A', 1), Tile('B', 2), Tile('?', 0)]
        self.assertEqual(player.find_joker(), 2)
    
    def test_no_find_joker(self):
        player = Player(name="Player 1")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.find_joker(), False)

if __name__ == "__main__":
    unittest.main()

class MockCell:
    def __init__(self, value):
        self.value = value

    def calculate_value(self):
        return self.value

if __name__ == "__main__":
    unittest.main()
