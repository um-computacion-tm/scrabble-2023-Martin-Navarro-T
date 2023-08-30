#test_player.py
import unittest
from game.player import Player
from game.models import BagTiles, Tile

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
        return self.letter.value

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

    def play_word(self, board, start_cell, word, direction):
        if not self.is_current_turn:
            return False

        cells_to_play = []  
        current_cell = start_cell

        for letter in word:
            if direction == 'horizontal':
                col = current_cell[1]
                cells_to_play.append((start_cell[0], col))
                current_cell = (current_cell[0], col + 1)
            else:
                row = current_cell[0] + 1
                cells_to_play.append((row, current_cell[1]))
                current_cell = (row, current_cell[1])

        word_multiplier = 1
        word_score = 0

        for cell_row, cell_col in cells_to_play:
            cell = board.grid[cell_row][cell_col]
            if cell.letter is not None:
                return False
            cell.add_letter(self.tiles.pop(0))
            word_score += cell.calculate_value()

        for cell_row, cell_col in cells_to_play:
            cell = board.grid[cell_row][cell_col]
            if cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier
            elif cell.multiplier_type == 'letter':
                word_score *= cell.multiplier

        self.score += word_score * word_multiplier

        self.is_current_turn = False
        return True


    def test_play_word(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4), Tile('E', 5)]
        
        board = MockBoard()
        player.start_turn()
        result = player.play_word(board, (7, 7), 'CAB', 'horizontal')
        self.assertTrue(result)
        self.assertEqual(player.score, 6)
        self.assertEqual(len(player.tiles), 2)
        self.assertFalse(player.is_current_turn)

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
    
    def test_play_word_invalid_turn(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4), Tile('E', 5)]
        
        board = MockBoard()
        result = player.play_word(board, (7, 7), 'CAB', 'horizontal')
        self.assertFalse(result)
        self.assertEqual(player.score, 0)
        self.assertEqual(len(player.tiles), 5)
        self.assertFalse(player.is_current_turn)
        
    def test_start_end_turn(self):
        player = Player(name='Player 1')
        
        player.start_turn()
        self.assertTrue(player.is_current_turn)
        
        player.end_turn()
        self.assertFalse(player.is_current_turn)

    def test_play_word_after_turn_end(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        
        board = MockBoard()
        player.start_turn()
        player.end_turn()
        
        result = player.play_word(board, (7, 7), 'ABC', 'horizontal')
        
        self.assertFalse(result)
        self.assertEqual(player.score, 0)
        self.assertEqual(len(player.tiles), 3)
        self.assertFalse(player.is_current_turn)
        
    def test_calculate_score_no_multipliers(self):
        player = Player(name='Player 1')
        cells = [MockCell(), MockCell(), MockCell()]
        player_score = player.calculate_score(cells)
        self.assertEqual(player_score, 0) 

if __name__ == '__main__':
    unittest.main()