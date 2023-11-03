#test_utils.py
import unittest
from game.utils import Utils  

class TestTuClase(unittest.TestCase):
    def test_increment_coordinates_horizontal(self):
        utils = Utils() 
        orientation = "Horizontal"
        row, column = utils.increment_coordinates(orientation, 1, 2)
        self.assertEqual(row, 1)
        self.assertEqual(column, 3)

    def test_increment_coordinates_vertical(self):
        utils = Utils()  
        orientation = "Vertical"
        row, column = utils.increment_coordinates(orientation, 1, 2)
        self.assertEqual(row, 2)
        self.assertEqual(column, 2)

    # word_to_tiles
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
        
if __name__ == '__main__':
    unittest.main()