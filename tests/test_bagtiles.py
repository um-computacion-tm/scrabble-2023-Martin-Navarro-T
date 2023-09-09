#test_bagtiles.py
import unittest
from game.tile import Tile
from game.bagtiles import BagTiles
from game.player import Player
from unittest.mock import patch

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            28,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        initial_tiles_count = len(bag.tiles)  
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            initial_tiles_count - len(tiles), 
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        initial_tiles_count = len(bag.tiles) 
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            initial_tiles_count + len(put_tiles), 
        )
    
    def test_initial_tiles(self):
        # Crea una instancia de la bolsa de fichas
        bag = BagTiles()

        # Llama al método initial_tiles
        bag.initial_tiles()

        # Define un diccionario con la cantidad esperada de fichas para cada letra
        expected_tiles_count = {
            'A': 11, 'E': 11, 'O': 8, 'I': 5, 'S': 5, 'N': 4, 'L': 3,
            'R': 4, 'U': 4, 'T': 3, 'D': 4, 'G': 1, 'C': 3, 'B': 1,
            'M': 1, 'P': 3, 'H': 1, 'Ñ': 8, 'F': 4, 'Y': 4, 'V': 4,
            'CH': 5, 'Q': 5, 'J': 8, 'LL': 8, 'X': 8, 'Z': 10,
            'RR': 8,  # Agregamos 'RR' con una cantidad de 8
        }

        # Inicializa un diccionario para contar la cantidad de fichas de cada letra
        actual_tiles_count = {letter: 0 for letter in expected_tiles_count.keys()}

        # Cuenta la cantidad de fichas de cada letra en la bolsa después de llamar a initial_tiles
        for tile in bag.tiles:
            actual_tiles_count[tile.letter] += 1

        # Realiza las aserciones para verificar que la cantidad de fichas es la esperada para cada letra
        for letter, count in expected_tiles_count.items():
            self.assertEqual(actual_tiles_count[letter], count)

if __name__ == '__main__':
    unittest.main()