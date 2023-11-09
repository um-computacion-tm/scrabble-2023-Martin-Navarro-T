#bagtiles.py
import random
from game.tile import Tile

class BagTiles:
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
            Tile('?', 0) #joker 
        ]
        random.shuffle(self.tiles)

    
    def initial_tiles(self):
        initial_tiles = {'A':12,'E':12,'O':9,'I':6,'S':6,'N':5,'L':4,'R':5,'U':5,'T':4,'D':5,'G':2,'C':4,'B':2,'M':2,'P':2,'H':2,'F':1,'V':1,'Y':1,'CH':1,'Q':1,'J':1,'LL':1,'Ñ':1,'RR':1,'X':1,'Z':1,'?':2}
        self.tiles = []
        for letter, amount in initial_tiles.items():
            self.put(Tile(letter, self.get_value_for_letter(letter)), amount)
        random.shuffle(self.tiles)
        
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles = self.tiles.pop(0)
        return tiles
    
    def put(self, tiles, amount=0):
        if amount == 0:
            self.tiles.extend(tiles)
        else:
            for i in range(amount):
                self.tiles.append(tiles)

    def get_value_for_letter(self, letter):
        bag = BagTiles()
        for tile in bag.tiles:
            if tile.letter == letter:
                return tile.value


    