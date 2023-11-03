# board.py
from game.cell import Cell
from game.utils import Utils
from game.dictionary import Dictionary

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
            [self.put_multipliers(multiplier) for multiplier in location_x]
            for location_x in board_multipliers
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
        

    def place_tile(self, location_x, location_y, tile): #
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False
    
    def validate_word(self, start_location_x, start_location_y, word, orientation): #
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

    def validate_word_inside_board(self,word, location, orientation):
        location_x = location[0]
        location_y = location[1]
        word_length = len(word)
        if orientation == "Horizontal":
            return location_y + word_length <= 15
        elif orientation == "Vertical":
            return location_x + word_length <= 15
        

    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)
    
    def process_tile_and_letter(self, tile, letter, list):
        utils = Utils()
        if utils.compare_tiles_and_letters(tile, letter) == 0:
            list[0].append(letter)
        elif utils.compare_tiles_and_letters(tile, letter) == 1:
            list[1].append(letter)
      
    def check_word_conditions(self, list):
        if len(list[0]) > 0:
            return False
        elif len(list[0]) == 0 and len(list[1]) > 0:
            return True
        elif len(list[0]) == 0 and len(list[1]) == 0:
            return True
        
    def validate_word_horizontal(self, word, location):
        utils = Utils()
        word = utils.word_to_tiles(word)
        location_x = location[0]
        location_y = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[location_x][location_y + i].letter
            self.process_tile_and_letter(actual_tile, word[i].letter, found_something)
        return self.check_word_conditions(found_something)

    def validate_word_vertical(self, word, location):
        utils = Utils()
        word = utils.word_to_tiles(word)
        location_x = location[0]
        location_y = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[location_x + i][location_y].letter
            self.process_tile_and_letter(actual_tile, word[i].letter, found_something)
        return self.check_word_conditions(found_something)

    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False

    def word_in_the_center(self, word, location, orientation):
        coordinate = {"Horizontal":location[0], "Vertical" : location[1]}
        central_coordinate = coordinate.get(orientation)
        if central_coordinate == 7:
            return self.validate_word_inside_board(word, location, orientation)
        else:
            return False

    def validate_word_place_board(self, word, location, orientation):
        if self.is_empty() is True:
           return self.word_in_the_center(word, location, orientation)
        else:
            if orientation == "Horizontal":
                return self.validate_word_horizontal(word, location)
            else:
                return self.validate_word_vertical(word, location) 

    # Agregar Función para Limpiar una Celda
    def clear_cell(self, location_x, location_y):
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is not None:
                cell.remove_letter()

    def put_words_board(self, word, location, orientation):
        utils = Utils()
        list_word = utils.word_to_tiles(word)
        location_x = location[0]
        location_y = location[1]
        i = 0
        for _ in list_word:
            self.grid[location_x][location_y].letter = list_word[i]
            self.grid[location_x][location_y].desactive_cell()
            location_x, location_y = utils.increment_coordinates(orientation, location_x, location_y)
            i += 1

    def horizontal_border_cells(self, length, location, list):
        location_x, location_y = location
        if location_y - 1 >= 0:
                list.append((location_x, location_y - 1))
        if location_y + length < 15:
                list.append((location_x, location_y + length))
    
    def vertical_border_cells(self, length, location, list):
        location_x, location_y = location
        if location_x - 1 >= 0:
            list.append((location_x - 1, location_y))
        if location_x + length < 15:
            list.append((location_x + length, location_y))
     
    def cells_around_horizontal_word(self, word, location, list):
        location_x, location_y = location
        word_length = len(word)
        self.horizontal_border_cells(word_length, location, list)
        for i in range(word_length):
            if location_x - 1 >= 0:
                list.append((location_x - 1, location_y + i))
            if location_x + 1 < 15:
                list.append((location_x + 1, location_y + i))
    
    def cells_around_vertical_word(self, word, location, list):
        location_x, location_y = location
        word_length = len(word)
        self.vertical_border_cells(word_length, location, list)
        for i in range(word_length):
            if location_y - 1 >= 0:
                list.append((location_x + i, location_y - 1))
            if location_y + 1 < 15:
                list.append((location_x + i, location_y + 1))
            
    def find_cells_around_word(self, word, location, orientation, adjacent_cells):
        if orientation == "Horizontal":
            self.cells_around_horizontal_word(word, location, adjacent_cells)
        elif orientation == "Vertical":
            self.cells_around_vertical_word(word, location, adjacent_cells)
    
    def find_tiles_around_word(self, orientation, adjacent_tiles, board):
        utils = Utils()
        if orientation == "Horizontal":
            adjacent_tiles = utils.filter_reapeted_column(adjacent_tiles)
            return utils.check_tiles_around_word(adjacent_tiles, 'Horizontal', board)
        elif orientation == "Vertical":
            adjacent_tiles = utils.filter_reapeted_row(adjacent_tiles)
            return utils.check_tiles_around_word(adjacent_tiles, 'Vertical', board)




