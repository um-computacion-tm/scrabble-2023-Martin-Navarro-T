# bagtiles.py
import random
from game.tile import Tile

class BagTiles:
    # Constructor
    def __init__(self):
        self.tiles = [
            Tile('A', 1),
            Tile('E', 1),
            Tile('O', 1),
            Tile('I', 1),
            Tile('S', 1),
            Tile('N', 1),
            Tile('L', 1),
            Tile('R', 1),
            Tile('U', 1),
            Tile('T', 1),
            Tile('D', 2),
            Tile('G', 2),
            Tile('C', 3),
            Tile('B', 3),
            Tile('M', 3),
            Tile('P', 3),
            Tile('H', 4),
            Tile('F', 4),
            Tile('V', 4),
            Tile('Y', 4),
            Tile('CH', 5),
            Tile('Q', 5),
            Tile('J', 8),
            Tile('LL', 8),
            Tile('Ñ', 8),
            Tile('RR', 8),
            Tile('X', 8),
            Tile('Z', 10),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles
    
    def put(self, tiles):
        self.tiles.extend(tiles)
        
    def initial_tiles(self):
        total = []
        initial_tiles = {
            'A': 11, 'E': 11, 'O': 8, 'I': 5, 'S': 5, 'N': 4, 'L': 3,
            'R': 4, 'U': 4, 'T': 3, 'D': 4, 'G': 1, 'C': 3, 'B': 1,
            'M': 1, 'P': 3, 'H': 1, 'Ñ': 8, 'F': 4, 'Y': 4, 'V': 4,
            'CH': 5, 'Q': 5, 'J': 8, 'LL': 8, 'X': 8, 'Z': 10,
            'RR': 8,  # Agregamos 'RR' con una cantidad de 8
        }
        
        # Crear un diccionario para contar cuántas fichas de cada letra tenemos en la bolsa actualmente
        current_tiles_count = {letter: 0 for letter in initial_tiles.keys()}

        # Contar las fichas actuales en la bolsa
        for tile in self.tiles:
            current_tiles_count[tile.letter] += 1

        # Agregar las fichas necesarias para que coincidan con las cantidades especificadas
        for letter, expected_count in initial_tiles.items():
            current_count = current_tiles_count[letter]
            if current_count < expected_count:
                # Agregar fichas adicionales para igualar la cantidad esperada
                for _ in range(expected_count - current_count):
                    total.append(Tile(letter, 1))  # Utilizar un valor fijo de 1 para el valor de las fichas

        # Extender la bolsa con las fichas adicionales
        self.tiles.extend(total)
