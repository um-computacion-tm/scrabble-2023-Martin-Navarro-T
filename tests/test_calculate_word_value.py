import unittest
from game.cell import Calculate_value 
from game.cell import Cell
from game.tile import Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
        ]
        
        letters = ["C", "A", "S", "A"]
        for i, cell in enumerate(word):
            cell.add_letter(Tile(letter=letters[i], value=1))

        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 4) 

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        for cell in word:
            cell.active = False  # Desactiva todas las celdas
        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 0)

    def test_with_letter_word_multiplier_active(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = Calculate_value.calculate_word_value(word)
        self.assertEqual(value, 14)
    
    def test_calculate_word_multiplier_with_word_multiplier(self):
        cell = Cell(value=5, multiplier_type='word', multiplier=3)
        result = Calculate_value.calculate_word_multiplier(cell)
        self.assertEqual(result, 3)  # Debería devolver el multiplicador de palabra, que es 3

    def test_calculate_word_multiplier_without_word_multiplier(self):
        cell = Cell(value=5, multiplier_type='letter', multiplier=2)
        result = Calculate_value.calculate_word_multiplier(cell)
        self.assertEqual(result, 1)  # Debería devolver 1 porque no es un multiplicador de palabra

    def test_calculate_word_value(self):
        cells = [
            Cell(value=3, multiplier_type='none', active=True, letter=Tile(letter='A', value=1)),
            Cell(value=2, multiplier_type='word', multiplier=2, active=True, letter=Tile(letter='B', value=2)),
            Cell(value=1, multiplier_type='letter', multiplier=3, active=True, letter=Tile(letter='C', value=3)),
        ]
        result = Calculate_value.calculate_word_value(cells)
        self.assertEqual(result, 24)  # Debería ser 3 * 1 + 2 * 2 * 3 * 3 = 24

    def test_calculate_cell_value_with_letter_multiplier(self):
        cell = Cell(multiplier=3, multiplier_type='letter', letter=Tile('A', 1), active=True)
        result = Calculate_value.calculate_cell_value(cell)
        self.assertEqual(result, 3)  # 1 (value) * 3 (multiplier)

    def test_calculate_cell_value_without_multiplier(self):
        cell = Cell(multiplier=1, multiplier_type='', letter=Tile('B', 2), active=True)
        result = Calculate_value.calculate_cell_value(cell)
        self.assertEqual(result, 2)  # 2 (value) * 1 (multiplier)

    def test_calculate_cell_value_empty_cell(self):
        cell = Cell()
        result = Calculate_value.calculate_cell_value(cell)
        self.assertEqual(result, 0)  # Celda vacía
        
if __name__ == '__main__':
    unittest.main()




