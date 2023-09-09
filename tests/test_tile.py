#test_tile.py
import unittest
from game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    
    def test_get_value_by_letter(self):
        # Crear una ficha con letra 'A' y valor 1
        tile_a = Tile('A', 1)
        # Verificar que el valor retornado sea 1 para la letra 'A'
        self.assertEqual(tile_a.get_value_by_letter('A'), 1)
        # Verificar que el valor retornado sea 0 para una letra diferente, por ejemplo, 'B'
        self.assertEqual(tile_a.get_value_by_letter('B'), 0)
        # Crear una ficha con letra 'Z' y valor 10
        tile_z = Tile('Z', 10)
        # Verificar que el valor retornado sea 10 para la letra 'Z'
        self.assertEqual(tile_z.get_value_by_letter('Z'), 10)
        # Verificar que el valor retornado sea 0 para una letra diferente, por ejemplo, 'X'
        self.assertEqual(tile_z.get_value_by_letter('X'), 0)

if __name__ == '__main__':
    unittest.main()