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

    def convert_result_to_list_of_words(self, result):
        words = []
        for list in result:
            words.append(list[0])
        return words

class ScrabbleUtils:
    def are_cells_around_word_valid(self, list_cell, list_tiles, board):
        total_of_coincidences = []
        for coord in list_cell:
            location_x, location_y = coord
            if board.grid[location_x][location_y].letter is not None:
                list_tiles.append((location_x, location_y))
                total_of_coincidences.append(1)
        if len(total_of_coincidences) > 0:
            return True
        else:
            return False

    def is_letter_multiplier_active(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_word_multiplier_active(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'
    
    def calculate_word_value(self,word):
        total_value = 0
        word_multiplier = 1

        for cell in word:
            if self.is_letter_multiplier_active(cell):
                total_value += cell.calculate_value()
            elif self.is_word_multiplier_active(cell):
                total_value += cell.calculate_value()
                word_multiplier *= cell.multiplier
            else:
                total_value += cell.letter.value
        total_value *= word_multiplier

        return total_value

    def increment_position(self, orientation, location_x, location_y):
        if orientation == "Horizontal":
            location_y += 1
        elif orientation == "Vertical":
            location_x += 1
        return location_x, location_y
    
    def generate_positions(self, word, location, orientation):
        positions = []
        location_x = location[0]
        location_y = location[1]
        for _ in word:
            positions.append((location_x, location_y))
            location_x, location_y = self.increment_position(orientation, location_x, location_y)
        return positions
    
    def collect_tiles_for_word(self, word, location, orientation, board):
        positions = self.generate_positions(word, location, orientation)
        list_tiles = []
        for position in positions:
            location_x, location_y = position
            tiles = board.grid[location_x][location_y].letter
            if tiles != None:
                list_tiles.append(tiles)
        return list_tiles

    def determine_required_tiles(self, word, location, orientation, board):
        utils = Utils()
        tiles_required = []
        word_tiles = utils.word_to_tiles(word)
        position_tiles = self.collect_tiles_for_word(word, location, orientation, board)
        position_set = set(tile.letter for tile in position_tiles)
        for tile in word_tiles:
            if tile.letter not in position_set:
                tiles_required.append(tile)
        return tiles_required
    
