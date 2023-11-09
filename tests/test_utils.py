import unittest
from game.utils import Utils, ScrabbleUtils
from game.board import Board
from game.cell import Cell
from game.tile import Tile

class TestUtils(unittest.TestCase):
    def test_word_to_tiles_simple_hola(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
        
    def test_word_to_tiles_simple_facultad(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("facultad")
        self.assertEqual(list_tiles[0].letter, "F")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "C")
        self.assertEqual(list_tiles[2].value, 2)
        self.assertEqual(list_tiles[3].letter, "U")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "L")
        self.assertEqual(list_tiles[4].value, 1)
        self.assertEqual(list_tiles[5].letter, "T")
        self.assertEqual(list_tiles[5].value, 1)
        self.assertEqual(list_tiles[6].letter, "A")
        self.assertEqual(list_tiles[6].value, 1)
        self.assertEqual(list_tiles[7].letter, "D")
        self.assertEqual(list_tiles[7].value, 2)
        
    def test_word_to_tiles_simple_casa(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
        
    def test_word_to_tiles_complex_CH(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("chita")
        self.assertEqual(list_tiles[0].letter, "CH")
        self.assertEqual(list_tiles[0].value, 5)
        self.assertEqual(list_tiles[1].letter, "I")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "T")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
        
    def test_word_to_tiles_complex_RR(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("perro")
        self.assertEqual(list_tiles[0].letter, "P")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "E")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "RR")
        self.assertEqual(list_tiles[2].value, 8)
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)
        
    def test_word_to_tilescomplex_LL(self):
        utils = Utils()
        list_tiles = utils.word_to_tiles("llanto")
        self.assertEqual(list_tiles[0].letter, "LL")
        self.assertEqual(list_tiles[0].value, 8)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "N")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "T")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "O")
        self.assertEqual(list_tiles[4].value, 1)
    
    def test_word_to_cells(self):
        utils = Utils()
        board = Board()
        word = 'llanto'
        location = (7,7)
        orientation = 'H'
        list_cell = utils.word_to_cells(word, location, orientation, board)
        self.assertEqual(list_cell[0].letter.letter, 'LL')
        self.assertEqual(list_cell[0].multiplier_type, 'word')
        self.assertEqual(list_cell[1].letter.letter, 'A')
        self.assertEqual(list_cell[2].letter.letter, 'N')
        self.assertEqual(list_cell[3].letter.letter, 'T')
        self.assertEqual(list_cell[4].letter.letter, 'O')

    def test_generate_positions_vertical(self):
        utils = Utils()
        word = "Facu"
        location = (4, 7)
        orientation = "V"
        result = utils.generate_positions(word,location, orientation)
        self.assertEqual(result, [(4,7), (5,7),(6,7),(7,7)])

    def test_generate_positions_horizontal(self):
        utils = Utils()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        result = utils.generate_positions(word,location, orientation)
        self.assertEqual(result, [(4,7), (4,8),(4,9),(4,10)])
        
    def test_remove_duplicate_columns(self):
        utils = Utils()
        list = [(7,7), (9,7)]
        list = utils.remove_duplicate_columns(list)
        self.assertEqual(list, [(7,7)])

    def test_remove_duplicate_rows(self):
        utils = Utils()
        list = [(7,7), (7,9)]
        list = utils.remove_duplicate_rows(list)
        self.assertEqual(list, [(7,7)])

class TestScrabbleUtils(unittest.TestCase):    
    def test_calculate_word_value_simple(self):
        utils2 = ScrabbleUtils()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = utils2.calculate_word_value(word)
        self.assertEqual(value,5)

    def test_calculate_word_value_with_letter_multiplier(self):
        utils2 = ScrabbleUtils()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A',1))
        ]
        value = utils2.calculate_word_value(word)
        self.assertEqual(value,7)
        
    def test_calculate_word_value_with_word_multiplier(self):
        utils2 = ScrabbleUtils()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = utils2.calculate_word_value(word)
        self.assertEqual(value,10)
        
    def test_calculate_word_value_with_word_and_letter_multiplier(self):
        utils2 = ScrabbleUtils()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = utils2.calculate_word_value(word)
        self.assertEqual(value,14)
        
    def test_calculate_word_value_with_word_and_letter_multiplier_no_active(self):
        utils2 = ScrabbleUtils()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = utils2.calculate_word_value(word)
        self.assertEqual(value,5)
      
    def test_collect_tiles_for_word(self):
        board = Board()
        utils2 = ScrabbleUtils()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        list_tiles = utils2.collect_tiles_for_word(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0].letter, 'A')
        self.assertEqual(list_tiles[1].letter, 'U')

    def test_collect_tiles_for_word_another_word_in_board(self):
        board = Board()
        utils2 = ScrabbleUtils()
        word = "hola"
        location = (6, 8)
        orientation = "V"
        board.put_words_board('hola', (7,7), 'H')
        list_tiles = utils2.collect_tiles_for_word(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 1)
        self.assertEqual(list_tiles[0].letter, 'O')

    def test_determine_required_tiles(self):
        board = Board()
        utils2 = ScrabbleUtils()
        word = "Facu"
        location = (4, 7)
        orientation = "H"
        board.grid[4][8] = Cell(letter=Tile('A',1))
        board.grid[4][10] = Cell(letter=Tile('U',1))
        list_tiles = utils2.determine_required_tiles(word,location, orientation, board)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0].letter, 'F')
        self.assertEqual(list_tiles[1].letter, 'C')
    
    def test_cells_around_horizontal_word(self):
        utils2 = ScrabbleUtils()
        word = "AB"
        location = (7,7)
        list = []
        utils2.cells_around_horizontal_word(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (7,6))
        self.assertEqual(list[1], (7,9))
        self.assertEqual(list[2], (6,7))
        self.assertEqual(list[3], (8,7))
        self.assertEqual(list[4], (6,8))
        self.assertEqual(list[5], (8,8))

    
    def test_cells_around_vertical_word(self):
        utils2 = ScrabbleUtils()
        word = "AB"
        location = (7,7)
        list = []
        utils2.cells_around_vertical_word(word,location,list)
        self.assertEqual(len(list), 6)
        self.assertEqual(list[0], (6,7))
        self.assertEqual(list[1], (9,7))
        self.assertEqual(list[2], (7,6))
        self.assertEqual(list[3], (7,8))
        self.assertEqual(list[4], (8,6))
        self.assertEqual(list[5], (8,8))
    
    def test_are_cells_around_word_valid(self):
        utils2 = ScrabbleUtils()
        board = Board()
        list_cell = [(6,7), (9,7), (7,6), (7,8), (8,6), (8,8)]
        list_tiles = []
        self.assertEqual(utils2.are_cells_around_word_valid(list_cell, list_tiles, board), False)
        self.assertEqual(len(list_tiles), 0)
    
    def test_are_cells_around_word_valid_true(self):
        utils2 = ScrabbleUtils()
        board = Board()
        board.grid[9][7] = Cell(letter=Tile('A',1))
        board.grid[7][8] = Cell(letter=Tile('B',1))
        list_cell = [(6,7), (9,7), (7,6), (7,8), (8,6), (8,8)]
        list_tiles = []
        self.assertEqual(utils2.are_cells_around_word_valid(list_cell, list_tiles, board), True)
        self.assertEqual(len(list_tiles), 2)
        self.assertEqual(list_tiles[0], (9,7))
        self.assertEqual(list_tiles[1], (7,8))