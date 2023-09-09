#test_player.py
import unittest
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile
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
        player = Player(name='Player 1')
        bag_tiles = BagTiles()
        
        player.draw_tiles(bag_tiles, 5)

        bag_tiles_count_before = len(bag_tiles.tiles)
        tiles_to_exchange = player.tiles[:2]  
        tiles_count_before = len(player.tiles)

        player.exchange_tiles(bag_tiles, tiles_to_exchange)
        self.assertEqual(len(player.tiles), tiles_count_before - 2 + len(tiles_to_exchange)) 
        self.assertEqual(len(bag_tiles.tiles), bag_tiles_count_before)
        
    def calculate_score(self, cells):
        score = 0
        word_multiplier = 1

        for cell in cells:
            cell_score = 0

            if cell.letter is not None:
                cell_score = cell.calculate_value()

                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier
                elif cell.multiplier_type == 'letter':
                    cell_score *= cell.multiplier

            score += cell_score

        return score * word_multiplier
    
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

if __name__ == '__main__':
    unittest.main()