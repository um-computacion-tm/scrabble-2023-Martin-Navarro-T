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
    
    def word_to_tiles(self, word):
        tiles_list = []
        i = 0
        while i < len(word):
            two_letter_combo = word[i:i+2]
            if two_letter_combo.upper() in ('CH', 'LL', 'RR'):
                self.convert_special_to_tiles(two_letter_combo, tiles_list)
                i += 2
            else:
                self.convert_string_to_tiles(word[i], tiles_list)
                i += 1
        return tiles_list
    
    def compare_tiles_and_letters(self, tile, letter):
        if tile is not None:
            if tile.letter == letter.upper():
                return 1
            else:
                return 0
        else:
            return
    
    def remove_duplicate_columns(self, list_tuples):
        columns = {}
        for location_x, location_y in list_tuples:
            if location_y not in columns:
                columns[location_y] = (location_x, location_y)
        list_tuples = list(columns.values())
        return list_tuples
    
    def remove_duplicate_rows(self, list_tuples):
        rows = {}
        for location_x, location_y in list_tuples:
            if location_x not in rows:
                rows[location_x] = (location_x, location_y)
        list_tuples = list(rows.values())
        return list_tuples
     
