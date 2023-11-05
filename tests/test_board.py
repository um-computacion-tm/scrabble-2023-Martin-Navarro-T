# test_board.py
import unittest
from game.board import Board
from game.tile import Tile
from game.cell import Cell
from game.utils import Utils, ScrabbleUtils

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

    def test_board_multiplier_word_in_board(self):
        board = Board()
        # Triple Word
        self.assertEqual(board.grid[0][0].multiplier, 3)
        self.assertEqual(board.grid[7][0].multiplier, 3)
        self.assertEqual(board.grid[14][0].multiplier, 3)
        self.assertEqual(board.grid[0][7].multiplier, 3)
        self.assertEqual(board.grid[0][14].multiplier, 3)
        self.assertEqual(board.grid[14][0].multiplier, 3)
        self.assertEqual(board.grid[14][7].multiplier, 3)
        self.assertEqual(board.grid[14][14].multiplier, 3)
        # Double Word
        self.assertEqual(board.grid[1][1].multiplier, 2)
        self.assertEqual(board.grid[2][2].multiplier, 2)
        self.assertEqual(board.grid[3][3].multiplier, 2)
        self.assertEqual(board.grid[4][4].multiplier, 2)
        self.assertEqual(board.grid[13][1].multiplier, 2)
        self.assertEqual(board.grid[12][2].multiplier, 2)
        self.assertEqual(board.grid[11][3].multiplier, 2)
        self.assertEqual(board.grid[10][4].multiplier, 2)
        self.assertEqual(board.grid[1][13].multiplier, 2)
        self.assertEqual(board.grid[2][12].multiplier, 2)
        self.assertEqual(board.grid[3][11].multiplier, 2)
        self.assertEqual(board.grid[4][10].multiplier, 2)
        self.assertEqual(board.grid[13][13].multiplier, 2)
        self.assertEqual(board.grid[12][12].multiplier, 2)
        self.assertEqual(board.grid[11][11].multiplier, 2)
        self.assertEqual(board.grid[10][10].multiplier, 2)
        self.assertEqual(board.grid[7][7].multiplier, 2)

    def test_board_multiplier_letter_in_board(self):
        board = Board()
        #Triple letter
        self.assertEqual(board.grid[1][5].multiplier, 3)
        self.assertEqual(board.grid[1][9].multiplier, 3)
        self.assertEqual(board.grid[5][1].multiplier, 3)
        self.assertEqual(board.grid[5][5].multiplier, 3)
        self.assertEqual(board.grid[5][13].multiplier, 3)
        self.assertEqual(board.grid[9][1].multiplier, 3)
        self.assertEqual(board.grid[9][5].multiplier, 3)
        self.assertEqual(board.grid[9][9].multiplier, 3)
        self.assertEqual(board.grid[9][13].multiplier, 3)
        self.assertEqual(board.grid[13][5].multiplier, 3)
        self.assertEqual(board.grid[13][9].multiplier, 3)
        # Double letter
        self.assertEqual(board.grid[0][3].multiplier, 2)
        self.assertEqual(board.grid[0][11].multiplier, 2)
        self.assertEqual(board.grid[2][6].multiplier, 2)
        self.assertEqual(board.grid[2][8].multiplier, 2)
        self.assertEqual(board.grid[3][0].multiplier, 2)
        self.assertEqual(board.grid[3][7].multiplier, 2)
        self.assertEqual(board.grid[3][14].multiplier, 2)
        self.assertEqual(board.grid[6][2].multiplier, 2)
        self.assertEqual(board.grid[6][6].multiplier, 2)
        self.assertEqual(board.grid[6][8].multiplier, 2)
        self.assertEqual(board.grid[6][12].multiplier, 2)
        self.assertEqual(board.grid[7][3].multiplier, 2)
        self.assertEqual(board.grid[7][11].multiplier, 2)
        self.assertEqual(board.grid[8][2].multiplier, 2)
        self.assertEqual(board.grid[8][6].multiplier, 2)
        self.assertEqual(board.grid[8][8].multiplier, 2)
        self.assertEqual(board.grid[8][12].multiplier, 2)
        self.assertEqual(board.grid[11][0].multiplier, 2)
        self.assertEqual(board.grid[11][7].multiplier, 2)
        self.assertEqual(board.grid[11][14].multiplier, 2)
        self.assertEqual(board.grid[12][6].multiplier, 2)
        self.assertEqual(board.grid[12][8].multiplier, 2)
        self.assertEqual(board.grid[14][3].multiplier, 2)
        self.assertEqual(board.grid[14][11].multiplier, 2)
     
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "Horizontal"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True

    def test_word_inside_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "Horizontal"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)
        
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5) 
        orientation = "Vertical"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)
 
    def test_word_out_of_board_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "Horizontal"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
        
    def test_word_out_of_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "Vertical"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertEqual(word_is_valid, False)
        
    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty(), True)
        
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7] = Tile('C', 1)
        self.assertEqual(board.is_empty(), False)
    
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
        
    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
        
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (4, 2)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_no_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 4)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_no_empty_board_horizontal_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        word = "Hola"
        location = (8, 5)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_no_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (4, 8)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_no_empty_board_vertical_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        word = "Hola"
        location = (5, 8)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_no_empthy_2_coincidence_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[8][8].add_letter(Tile('L',1))
        board.grid[9][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (7,5)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_no_empthy_2_coincidence_horizontal_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[8][7].add_letter(Tile('A',1))
        board.grid[9][7].add_letter(Tile('S',1))
        board.grid[10][7].add_letter(Tile('A',1))
        board.grid[7][8].add_letter(Tile('M',1))
        board.grid[8][8].add_letter(Tile('A',1))
        board.grid[9][8].add_letter(Tile('L',1))
        word = "Foca"
        location = (7,5)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_no_empthy_2_coincidence_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        board.grid[8][6].add_letter(Tile('A',1))
        board.grid[8][7].add_letter(Tile('L',1))
        board.grid[8][8].add_letter(Tile('A',1))
        word = "Foca"
        location = (5,7)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_no_empthy_2_coincidence_vertical_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C',1))
        board.grid[7][8].add_letter(Tile('A',1))
        board.grid[7][9].add_letter(Tile('S',1))
        board.grid[7][10].add_letter(Tile('A',1))
        board.grid[8][7].add_letter(Tile('M',1))
        board.grid[8][8].add_letter(Tile('A',1))
        board.grid[8][9].add_letter(Tile('L',1))
        word = "Foca"
        location = (5,7)
        orientation = "Vertical"

        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_place_word_complex(self):
        board = Board()
        board.put_words_board("Facu", (5,7), "Horizontal")
        board.put_words_board("Hola", (2,8), "Vertical")
        self.assertEqual(board.validate_word_place_board("Lacra", (3,9), "Vertical"), False)

    def test_put_words_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "Horizontal"
        board.put_words_board(word, location, orientation)
        self.assertEqual(board.grid[5][4].letter.letter, "F")
        self.assertEqual(board.grid[5][5].letter.letter, "A")
        self.assertEqual(board.grid[5][6].letter.letter, "C")
        self.assertEqual(board.grid[5][7].letter.letter, "U")
        self.assertEqual(board.grid[5][8].letter.letter, "L")
        self.assertEqual(board.grid[5][9].letter.letter, "T")
        self.assertEqual(board.grid[5][10].letter.letter, "A")
        self.assertEqual(board.grid[5][11].letter.letter, "D")
    
    def test_put_words_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "Vertical"
        board.put_words_board(word, location, orientation)
        self.assertEqual(board.grid[5][4].letter.letter, "F")
        self.assertEqual(board.grid[6][4].letter.letter, "A")
        self.assertEqual(board.grid[7][4].letter.letter, "C")
        self.assertEqual(board.grid[8][4].letter.letter, "U")
        self.assertEqual(board.grid[9][4].letter.letter, "L")
        self.assertEqual(board.grid[10][4].letter.letter, "T")
        self.assertEqual(board.grid[11][4].letter.letter, "A")
        self.assertEqual(board.grid[12][4].letter.letter, "D") 

    def test_cells_around_horizontal_word(self):
        board = Board()
        word = "AB"
        location = (7,7)
        list = []
        board.cells_around_horizontal_word(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (7,6))
        self.assertEqual(list[1], (7,9))
        self.assertEqual(list[2], (6,7))
        self.assertEqual(list[3], (8,7))
        self.assertEqual(list[4], (6,8))
        self.assertEqual(list[5], (8,8))

    
    def test_cells_around_vertical_word(self):
        board = Board()
        word = "AB"
        location = (7,7)
        list = []
        board.cells_around_vertical_word(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (6,7))
        self.assertEqual(list[1], (9,7))
        self.assertEqual(list[2], (7,6))
        self.assertEqual(list[3], (7,8))
        self.assertEqual(list[4], (8,6))
        self.assertEqual(list[5], (8,8))

    def test_cross_word_right_way(self):
        board = Board()
        board.grid[7][7] = Cell(1, '', Tile('H', 1))
        board.grid[7][8] = Cell(1, '', Tile('O', 1))   
        board.grid[7][9] = Cell(1, '', Tile('L', 1))   
        board.grid[7][10] = Cell(1, '', Tile('A', 1))       
        self.assertTrue(board.validate_word_place_board('CAMA', (6,10), 'Vertical'))
    
    def test_cross_word_wrong_way(self):
        board = Board()
        board.grid[7][7] = Cell(1, '', Tile('H', 1))
        board.grid[7][8] = Cell(1, '', Tile('O', 1))   
        board.grid[7][9] = Cell(1, '', Tile('L', 1))   
        board.grid[7][10] = Cell(1, '', Tile('A', 1))       
        self.assertFalse(board.validate_word_place_board('CAMA', (6,8), 'Vertical'))


if __name__ == '__main__':
    unittest.main()
