# player.py
from game.bagtiles import BagTiles

class Player:
    def __init__(self, name, id=0, bag_tiles=None):
        self.name = name #
        self.id = id
        self.score = 0
        self.rack = []
 
    def exchange_tiles(self,index,bag=BagTiles):
        index = index - 1
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.insert(index, new_tile)

    def has_letters(self, tiles):
        rack = set(tile.letter for tile in self.rack) 
        return set(tile.letter for tile in tiles).issubset(rack) 
        
    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))
    
    def has_joker(self):
        for tile in self.rack:
            if tile.is_joker() is True:
                return True
        return False
    
    def find_joker(self):
        for i, tile in enumerate(self.rack):
            if tile.is_joker() is True:
                return i
        return False
    