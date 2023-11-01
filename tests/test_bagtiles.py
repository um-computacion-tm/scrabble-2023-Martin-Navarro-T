import unittest
from game.tile import Tile
from game.bagtiles import BagTiles, NoTilesAvailable, ImpossibleToChangeMoreThan7, BagFull
from game.player import Player
from unittest.mock import patch

class TestBagTiles(unittest.TestCase):
    #NEw
    @patch('random.shuffle')
    def test_bag_tiles(self,patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),29)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.tiles)
        
    def test_initial_tiles(self):
        bag = BagTiles()
        bag.initial_tiles()
        self.assertEqual(len(bag.tiles),100)
        
    def test_take(self):
        bag = BagTiles()
        initial_tiles_count = len(bag.tiles)  

        # Vaciar la bolsa tomando todas las fichas
        taken_tiles = bag.take(initial_tiles_count)

        # Intentar tomar una ficha adicional, lo que debería generar la excepción NoHayFichas
        with self.assertRaises(NoTilesAvailable):
            bag.take(1)

        self.assertEqual(
            len(bag.tiles),
            0,  # La bolsa debería estar vacía después de tomar todas las fichas
        )
        self.assertEqual(
            len(taken_tiles),
            initial_tiles_count,  # Deberías haber tomado todas las fichas
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        initial_tiles_count = len(bag.tiles) 

        # Llenar la bolsa hasta que esté completa
        while len(bag.tiles) < 100:
            bag.put([Tile('A', 1)])
        
        # Prueba la excepción BolsaLlena cuando intentas poner fichas en una bolsa llena
        with self.assertRaises(BagFull):
            bag.put(put_tiles)

        # Intentar poner más de 7 fichas a la vez, lo que debería generar la excepción ImposibleCambiarMasDe7
        with self.assertRaises(ImpossibleToChangeMoreThan7):
            bag.put([Tile('B', 1)] * 8)  # Intentar poner 8 fichas a la vez

        # La bolsa no debería haber cambiado en estas pruebas
        self.assertEqual(
            len(bag.tiles),
            100,  # La bolsa debería seguir llena
        )

    def test_put_more_than_7_tiles(self):
        bag = BagTiles()
        put_tiles = [Tile('A', 1)] * 8  # Intentar poner 8 fichas a la vez
        with self.assertRaises(ImpossibleToChangeMoreThan7):
            bag.put(put_tiles)

    def test_put_bag_full(self):
        bag = BagTiles()
        put_tiles = [Tile('A', 1)]
        # Llenar la bolsa hasta que esté completa
        while len(bag.tiles) < 100:
            bag.put([Tile('B', 1)])
        # Intentar poner una ficha más, lo que debería generar la excepción BolsaLlena
        with self.assertRaises(BagFull):
            bag.put(put_tiles)
            
    def test_get_value_by_letter(self):
        bag = BagTiles()
        self.assertEqual(bag.get_value_by_letter('A'), 1)
        self.assertEqual(bag.get_value_by_letter('B'), 3)
        self.assertEqual(bag.get_value_by_letter('C'), 2)
        self.assertEqual(bag.get_value_by_letter('E'), 1)
        self.assertEqual(bag.get_value_by_letter('?'), 0)

if __name__ == '__main__':
    unittest.main()
