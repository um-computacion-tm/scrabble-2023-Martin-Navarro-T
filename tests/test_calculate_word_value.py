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

if __name__ == '__main__':
    unittest.main()
