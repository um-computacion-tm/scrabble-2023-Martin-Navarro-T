#player.py
class Player:
    def __init__(self):
        self.tiles = []

    def draw_tiles(self, bag_tiles, count):
        new_tiles = bag_tiles.take(count)
        self.tiles.extend(new_tiles)

    def exchange_tiles(self, bag_tiles, tiles_to_exchange):
        tiles_to_keep = [tile for tile in self.tiles if tile not in tiles_to_exchange]
        tiles_taken = bag_tiles.take(len(tiles_to_exchange))
        
        bag_tiles.put(tiles_to_exchange)  
        self.tiles = tiles_to_keep + tiles_taken


    def calculate_score(self, cells):
        score = 0
        word_multiplier = 1

        for cell in cells:
            cell_score = 0

            if cell.letter is not None:
                cell_score = cell.calculate_value()

                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier
                elif cell.multiplier_type == 'letter':
                    cell_score *= cell.multiplier

            score += cell_score

        return score * word_multiplier
