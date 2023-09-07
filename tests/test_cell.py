# test_cell.py
import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )
    
    def test_remove_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        removed_letter = cell.remove_letter()

        self.assertEqual(cell.letter, None)
        self.assertEqual(removed_letter, letter)
    
    #newww
    def test_inactive_cell(self):
        # Crear una celda que no está activa
        cell = Cell(letter=Tile('A', 1))
        cell.active = False  # Establecer la celda como no activa

        # Intentar calcular el valor de la celda no activa
        calculator = cell.calculate_value()

        # Asegurarse de que el valor calculado sea 0
        self.assertEqual(calculator, 0)
if __name__ == '__main__':
    unittest.main()

