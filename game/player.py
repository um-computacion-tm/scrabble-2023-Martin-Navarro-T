# player.py
from game.bagtiles import BagTiles

class Player:
    def __init__(self, name, bag_tiles=None):
        self.name = name
        self.tiles = []
        self.score = 0
        self.is_current_turn = False
        self.bag_tiles = bag_tiles
        self.rack = []
        #self.played_words = []  # Lista para llevar un registro de las palabras jugadas
        
    def draw_tiles(self, bag, num_tiles):
        if num_tiles <= len(bag.tiles):
            self.tiles.extend(bag.tiles[:num_tiles])
            del bag.tiles[:num_tiles]

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
  
    def view_tiles(self):
        return self.tiles[:]

    def view_score(self):
        return self.score

    def start_turn(self):
        self.is_current_turn = True

    def end_turn(self):
        self.is_current_turn = False

    def pass_turn(self):
        self.end_turn()

    def check_tile_in_hand(self, tile):
        return tile in self.tiles

    def get_hand_size(self):
        return len(self.tiles)

    def get_score(self):
        total_score = 0
        for cell in self.board.played_cells:
            total_score += cell.calculate_value()
        return total_score

    def has_letters(self, tiles):
        rack = set(tile.letter for tile in self.rack) #Creación de un cojunto de python
        return set(tile.letter for tile in tiles).issubset(rack) #Se crea otro conjunto de python 
        #issubset comprueba si el nuevo conjunto es un subconjunto de rack, si es así devuelve True
        
    def set_tiles(self, tiles):
        self.tiles = tiles
        
    def get_tiles(self):
        return self.tiles
