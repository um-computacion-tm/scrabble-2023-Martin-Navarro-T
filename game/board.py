# board.py
from game.cell import Cell
from game.tile import Tile

class Board:
    def __init__(self):
        board_multipliers = [
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"],
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None], 
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            ["3W", None, None, "2L", None, None, None, "2W", None, None, None, "2L", None, None, "3W"],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None],  
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"] 
        ]
        self.grid = [
            [self.put_multipliers(multiplier) for multiplier in row]
            for row in board_multipliers
        ]

    def put_multipliers(self, multiplier):
        if multiplier is None:
            return Cell()
        multiplier_type = multiplier[-1]
        multiplier_value = int(multiplier[0])
        if multiplier_type == "W":
            return Cell(multiplier=multiplier_value, multiplier_type="word")
        elif multiplier_type == "L":
            return Cell(multiplier=multiplier_value, multiplier_type="letter")

    def place_tile(self, location_x, location_y, tile):
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False
    
    def validate_word(self, start_location_x, start_location_y, word, orientation):
        for i, letter in enumerate(word):
            if orientation == 'Horizontal':
                location_x = start_location_x
                location_y = start_location_y + i
            elif orientation == 'Vertical':
                location_x = start_location_x + i
                location_y = start_location_y

            if location_x >= 15 or location_y >= 15 or (self.grid[location_x][location_y].letter is None or self.grid[location_x][location_y].letter.letter != letter):
                return False
        return True

    def validate_word_inside_board(self, word, location, orientation):
        location_x, location_y = location
        word_length = len(word)

        if orientation == "Horizontal":
            return location_y + word_length <= 15
        elif orientation == "Vertical":
            return location_x + word_length <= 15
        #else:
         #   return InvalidWordPlacement(Exception)

    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)

    def validate_word_horizontal(self, word, location, orientation):
        location_x, location_y = location
        word_length = len(word)
        found_letter = False

        for i in range(word_length):
            actual_tile = self.grid[location_x][location_y + i].letter
            if actual_tile is not None and actual_tile.letter.lower() == word[i]:
                found_letter = True

        return found_letter and self.validate_word_inside_board(word, location, orientation)

    def validate_word_vertical(self, word, location, orientation):
        location_x, location_y = location
        word_length = len(word)
        found_letter = False
        for i in range(word_length):
            actual_tile = self.grid[location_x + i][location_y].letter
            if actual_tile is not None:
                if actual_tile.letter.lower() == word[i]:
                    found_letter = True
        return found_letter and self.validate_word_inside_board(word, location, orientation)

    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False

    def word_in_the_center(self, word, location, orientation):
        location_x, location_y = location
        is_horizontal = orientation == "Horizontal"
        is_vertical = orientation == "Vertical"

        if is_horizontal and location_x == 7:
            return self.validate_word_inside_board(word, location, orientation)

        if is_vertical and location_y == 7:
            return self.validate_word_inside_board(word, location, orientation)

        return False

    def validate_word_place_board(self, word, location, orientation):
        if self.is_empty() is True:
            return self.word_in_the_center(word, location, orientation)
        else:
            if orientation == "Horizontal":
                return self.validate_word_horizontal(word, location, orientation)
            else:
                return self.validate_word_vertical(word, location, orientation)

    # Agregar Función para Limpiar una Celda
    def clear_cell(self, location_x, location_y):
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is not None:
                cell.remove_letter()