#test_tile.py
import unittest
from game.tile import Tile, NotAJoker

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

    def test_joker_with_valid_letter(self):
        # Crear una ficha comodín con letra '*'
        tile = Tile('*', 0)
        
        # Cambiar la letra del comodín a 'A'
        tile.joker('A')
        
        # Verificar que la letra de la ficha sea 'A' después del cambio
        self.assertEqual(tile.letter, 'A')
    
    def test_joker_with_invalid_letter(self):
        # Crear una ficha no comodín con letra 'B'
        tile = Tile('B', 1)
        
        # Intentar cambiar la letra de la ficha no comodín a 'A' debería lanzar la excepción NoEsUnJoker (NotAJoker)
        with self.assertRaises(NotAJoker):
            tile.joker('A')

if __name__ == '__main__':
    unittest.main()