#test_tile.py
import unittest
from game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    
    def test_is_joker(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_joker(), True)
    
    def test_is_not_joker(self):
        tile = Tile('A', 1)  # Cualquier letra que no sea un comodín, por ejemplo, 'A'
        self.assertEqual(tile.is_joker(), False)

    def test_convert_tile(self):
        tile = Tile('A',1)
        tile.convert_tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)
        
if __name__ == '__main__':
    unittest.main()