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

if __name__ == '__main__':
    unittest.main()
