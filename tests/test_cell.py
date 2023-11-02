# test_cell.py
import unittest
from game.cell import Cell
from game.tile import Tile

class TestCell(unittest.TestCase):
    def test_cell(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,'letter')
        self.assertEqual(cell.letter, None)
    
    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)
    
    def test_remove_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        removed_letter = cell.remove_letter()
        self.assertEqual(cell.letter, None)
        self.assertEqual(removed_letter, letter)
    
    def test_cell_value(self):
        cell = Cell(multiplier=1, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(), 3)
    
    def test_cell_multiplayer_letter(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

    def test_cell_multiplayer_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3,)

    def test_cell_letter(self):
        cell = Cell(1, None)
        self.assertEqual(cell.calculate_value(),0)
    
    def test_desactive(self):
        cell = Cell()
        self.assertEqual(cell.status, "active")
        cell.desactive_cell()
        self.assertEqual(cell.status, "desactive")
    
    def test_reset_cell(self):
        cell = Cell(3, 'word')
        cell.multiplier = 1
        cell.multiplier_type = ''
        cell.status = 'desactive'
        cell.letter = Tile('H',1)
        cell.reset_cell()
        self.assertEqual(cell.multiplier, 3)
        self.assertEqual(cell.multiplier_type, 'word')
        self.assertEqual(cell.status, 'active')
        self.assertEqual(cell.letter, None)
    
    def test_repr_with_letter(self):
        cell = Cell(letter="A")
        expected_repr = "'A'"
        self.assertEqual(repr(cell), expected_repr)

    def test_repr_word_multiplier(self):
        cell = Cell(multiplier=2, multiplier_type="word")
        expected_repr = 'Wx2'
        self.assertEqual(repr(cell), expected_repr)

    def test_repr_letter_multiplier(self):
        cell = Cell(multiplier=3, multiplier_type="letter")
        expected_repr = 'Lx3'
        self.assertEqual(repr(cell), expected_repr)
    
    def test_repr_empty(self):
        cell = Cell()
        expected_repr = '   '
        self.assertEqual(repr(cell), expected_repr)       
        
if __name__ == '__main__':
    unittest.main()