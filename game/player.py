# player.py
class Player:
    def __init__(self, name, bag_tiles=None):
        self.name = name
        self.tiles = []
        self.score = 0
        self.is_current_turn = False
        self.bag_tiles = bag_tiles
        
    def draw_tiles(self, bag_tiles, count):
        new_tiles = bag_tiles.take(count)
        self.tiles.extend(new_tiles)

    def exchange_tiles(self, bag_tiles, tiles_to_exchange):
        tiles_to_keep = [tile for tile in self.tiles if tile not in tiles_to_exchange]
        tiles_taken = bag_tiles.take(len(tiles_to_exchange))
        
        bag_tiles.put(tiles_to_exchange)  
        self.tiles = tiles_to_keep + tiles_taken

    def view_tiles(self):
        return self.tiles[:]

    def view_score(self):
        return self.score

    def start_turn(self):
        self.is_current_turn = True

    def end_turn(self):
        self.is_current_turn = False
    
