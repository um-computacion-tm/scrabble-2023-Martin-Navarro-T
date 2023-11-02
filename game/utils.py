#utils.py
from game.bagtiles import BagTiles

class Utils:
    def convert_string_to_tiles(self, input_string, list):
        bag = BagTiles()
        letter_set = set(tile.letter for tile in bag.tiles)
        for letter in input_string.upper():
            if letter in letter_set:
                matching_tile = next(tile for tile in bag.tiles if tile.letter == letter)
                list.append(matching_tile)

    def convert_special_to_tiles(self, input_string, list):
        bag = BagTiles()
        for tile in bag.tiles:
            if tile.letter == input_string.upper():
                list.append(tile)
                break
        
    def increment_coordinates(self, orientation, row, column): 
        if orientation == "Horizontal":
            column += 1
        elif orientation == "Vertical":
            row += 1
        return row, column
