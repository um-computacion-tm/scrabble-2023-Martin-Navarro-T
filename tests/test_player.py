#test_player.py
import unittest
from game.player import Player
from game.models import BagTiles, Tile

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
        
    def test_draw_tiles(self):
        player = Player()
        bag_tiles = BagTiles()

        player.draw_tiles(bag_tiles, 5)
        self.assertEqual(len(player.tiles), 5)

    def test_exchange_tiles(self):
        player = Player()
        bag_tiles = BagTiles()
        
        player.draw_tiles(bag_tiles, 5)

        bag_tiles_count_before = len(bag_tiles.tiles)
        tiles_to_exchange = player.tiles[:2]  
        tiles_count_before = len(player.tiles)

        player.exchange_tiles(bag_tiles, tiles_to_exchange)
        self.assertEqual(len(player.tiles), tiles_count_before - 2 + len(tiles_to_exchange)) 
        self.assertEqual(len(bag_tiles.tiles), bag_tiles_count_before)



    def test_calculate_score(self):
        player = Player()

        class MockCell:
            def __init__(self, letter, multiplier, multiplier_type):
                self.letter = letter
                self.multiplier = multiplier
                self.multiplier_type = multiplier_type

            def calculate_value(self):
                return self.letter.value

        cells = [
            MockCell(Tile('A', 1), 1, ''),
            MockCell(Tile('B', 2), 2, 'letter'),
            MockCell(Tile('C', 3), 1, 'word'), 
        ]

        score = player.calculate_score(cells)
        expected_score = (1 * 1) + (2 * 2) + (3 * 1)
        self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()

