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

        self.tiles = [
            Tile('A', 1),
            Tile('B', 3),
            Tile('C', 2),
            Tile('CH', 5),
            Tile('D', 2),
            Tile('E', 1),
            Tile('F', 4),
            Tile('G', 2),
            Tile('H', 4),
            Tile('I', 1),
            Tile('J', 6),
            Tile('L', 1),
            Tile('LL', 8),
            Tile('M', 3),
            Tile('N', 1),
            Tile('Ñ', 8),
            Tile('O', 1),
            Tile('P', 2),
            Tile('Q', 8),
            Tile('R', 1),
            Tile('RR', 8),
            Tile('S', 1),
            Tile('T', 1),
            Tile('U', 1),
            Tile('V', 4),
            Tile('X', 8),
            Tile('Y', 4),
            Tile('Z', 10),
            Tile('?', 0)
        ]
        random.shuffle(self.tiles)

    def initial_tiles(self):
        total = []
        bag = BagTiles()
        initial_tiles = {'A': 11, 'E': 11, 'O': 8, 'I': 5, 'S': 5, 'N': 4, 'L': 3, 'R': 4, 'U': 4, 'T': 3, 'D': 4, 'G': 1, 'C': 3, 'B': 1, 'M': 1, 'P': 1, 'H': 1, '?': 1}
        while len(total) < 71:
            for letter, amount in initial_tiles.items():
                new_tiles = [x for x in bag.tiles if x.letter == letter]
                count = min(amount, 100 - len(total))
            total.extend(new_tiles[:count])
        self.tiles.extend(total)

    def take(self, count):
        if len(self.tiles) < count:
            raise NoTilesAvailable("No hay suficientes fichas disponibles en la bolsa.")
        
        tiles = [self.tiles.pop() for _ in range(count)]
        return tiles
    
    def put(self, tiles):
        if len(tiles) > 7:
            raise ImpossibleToChangeMoreThan7("No se pueden cambiar más de 7 fichas a la vez.")
        
        if len(self.tiles) + len(tiles) > 100:
            raise BagFull("La bolsa está llena y no se pueden agregar más fichas.")
        
        self.tiles.extend(tiles)