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

        self.assertTrue(board.validate_word(7, 7, 'ABC', 'Horizontal'))
        self.assertFalse(board.validate_word(7, 7, 'ACB', 'Horizontal'))
        self.assertTrue(board.validate_word(7, 7, 'A', 'Vertical'))
        self.assertFalse(board.validate_word(7, 7, 'AB', 'Vertical'))
        
    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == True
    

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "Horizontal"

        word_is_valid = board.validate_word_out_of_board(word, location, orientation)

        assert word_is_valid == False

    def test_word_inside_board_vertical(self):
        board = Board()
        word = "Facultad"
        location = (4, 5) 
        orientation = "Vertical"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        self.assertTrue(word_is_valid)
        

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
        board.put_words_board("Facu", (5,7), "H")
        board.put_words_board("Hola", (2,8), "V")
        self.assertEqual(board.validate_word_place_board("Lacra", (3,9), "V"), False)

    # Tets de Agregar Función para Limpiar una Celda
    def test_clear_cell_valid(self):
        board = Board()
        tile = Tile('A', 1)

        # Colocamos una ficha en una celda
        board.place_tile(7, 7, tile)
        # Luego la limpiamos
        board.clear_cell(7, 7)
        # Comprobamos que la celda esté vacía
        self.assertIsNone(board.grid[7][7].letter)

    def test_clear_cell_invalid(self):
        board = Board()

        # Intentamos limpiar una celda fuera de los límites
        result = board.clear_cell(16, 16)
        # Debería devolver False ya que la celda está fuera de los límites
        self.assertFalse(result)

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
        
if __name__ == "__main__":
    unittest.main()
