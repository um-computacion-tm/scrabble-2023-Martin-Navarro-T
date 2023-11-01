import unittest
from unittest.mock import Mock, patch
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile
from game.board import Board
from game.cell import Cell

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player1 = Player(name='Martin')
        self.assertEqual(player1.rack,[])
    
    def test_player_get_tile(self):
        bag1 = BagTiles()
        player = Player(name='Martin')
        player.get_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    def test_exchange_tiles(self):
        bag1 = BagTiles()
        player = Player(name='Martin')
        player.rack = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        player.exchange_tiles(2, bag1)
        self.assertEqual(len(player.rack), 3)
        self.assertEqual(len(bag1.tiles), 29)

    def test_validate_rack_true(self):
        player_1 = Player(name='Martin')
        tiles = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1)]
        player_1.rack = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1), Tile("Z", 1), Tile("Z", 1), Tile("Z", 1)]
        is_valid = player_1.has_letters(tiles)
        self.assertTrue(is_valid)

    def test_validate_rack_false(self):
        player_1 = Player(name='Martin')
        tiles = [Tile("H", 1), Tile("O", 1), Tile("L", 1), Tile("A", 1)]
        player_1.rack = [Tile("H", 1), Tile("O", 1), Tile("E", 1), Tile("A", 1), Tile("Z", 1), Tile("Z", 1), Tile("Z", 1)]
        is_valid = player_1.has_letters(tiles)
        self.assertFalse(is_valid)

    def test_has_joker_true(self):
        player = Player(name="Martin")
        player.rack = [Tile('A', 1), Tile('?', 0)]
        self.assertEqual(player.has_joker(), True)

    def test_has_joker_false(self):
        player = Player(name="Martin")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.has_joker(), False)
    
    def test_find_joker(self):
        player = Player(name="Martin")
        player.rack = [Tile('A', 1), Tile('B', 2), Tile('?', 0)]
        self.assertEqual(player.find_joker(), 2)
    
    def test_no_find_joker(self):
        player = Player(name="Martin")
        player.rack = [Tile('A', 1), Tile('B', 2)]
        self.assertEqual(player.find_joker(), False)

if __name__ == "__main__":
    unittest.main()

