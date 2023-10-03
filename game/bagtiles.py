# bagtiles.py
import random
from game.tile import Tile

# Excepciones
# Si no hay fichas
class NoTilesAvailable(Exception):
    pass
#Si quiere cambiar mas de 7 fichas
class ImpossibleToChangeMoreThan7(Exception):
    pass
#Si la bolsa esta llena
class BagFull(Exception):
    pass

class BagTiles:
    # Constructor
    def __init__(self):
        self.tiles = []

        tile_info = [
            ('A', 1, 12), 
            ('E', 1, 12), 
            ('O', 1, 9),
            ('I', 1, 6), 
            ('S', 1, 6), 
            ('N', 1, 5),
            ('L', 1, 4), 
            ('R', 1, 5), 
            ('U', 1, 5),
            ('T', 1, 4), 
            ('D', 2, 5), 
            ('G', 2, 2),
            ('C', 3, 4), 
            ('B', 3, 2), 
            ('M', 3, 2),
            ('P', 3, 2), 
            ('H', 4, 2), 
            ('F', 4, 1),
            ('V', 4, 1), 
            ('Y', 4, 1), 
            ('J', 8, 1),
            ('CH',5,1),
            ('Q',5,1),
            ('LL', 8, 1), 
            ('Ñ', 8, 1), 
            ('RR', 8, 1),
            ('X', 8, 1), 
            ('Z', 10, 1),
            (' ', 0, 2)  # Comodines en blanco
        ]

        for letter, value, count in tile_info:
            self.tiles.extend([Tile(letter, value)] * count)

        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        if len(self.tiles) == 0:
            raise NoTilesAvailable(Exception)
        else:
            for _ in range(count):
                tiles.append(self.tiles.pop())
            return tiles
    
    def put(self, tiles):
        if len(tiles) > 7:
            raise ImpossibleToChangeMoreThan7(Exception)
        elif len(self.tiles) == 100:
            raise BagFull(Exception)
        else:
            self.tiles.extend(tiles)