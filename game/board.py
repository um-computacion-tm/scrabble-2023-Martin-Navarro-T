#board.py
from game.cell import Cell
from game.dictionary import Dictionary
from game.utils import Utils, ScrabbleUtils

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

    def validate_word_inside_board(self,word, location, orientation):
        row = location[0]
        column = location[1]
        word_length = len(word)
        if orientation == "H":
            return column + word_length <= 15
        elif orientation == "V":
            return row + word_length <= 15
        
    def process_tile_and_letter(self, tile, letter, list):
        utils2 = ScrabbleUtils()
        if utils2.compare_tiles_and_letters(tile, letter) == 0:
            list[0].append(letter)
        elif utils2.compare_tiles_and_letters(tile, letter) == 1:
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
        row = location[0]
        column = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[row][column + i].letter
            self.process_tile_and_letter(actual_tile, word[i].letter, found_something)
        return self.check_word_conditions(found_something)
    
    def validate_word_vertical(self, word, location):
        utils = Utils()
        word = utils.word_to_tiles(word)
        row = location[0]
        column = location[1]
        found_coincidences = []
        found_problem = []
        found_something = [found_problem, found_coincidences]
        for i in range(len(word)):
            actual_tile = self.grid[row + i][column].letter
            self.process_tile_and_letter(actual_tile, word[i].letter, found_something)
        return self.check_word_conditions(found_something)
        
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False       
        
    def word_in_the_center(self, word, location, orientation):
        coordinate = {"H":location[0], "V" : location[1]}
        central_coordinate = coordinate.get(orientation)
        if central_coordinate == 7:
            return self.validate_word_inside_board(word, location, orientation)
        else:
            return False  
        
    def validate_word_place_board(self, word, location, orientation):
        if self.is_empty() is True:
           return self.word_in_the_center(word, location, orientation)
        else:
            if orientation == "H":
                return self.validate_word_horizontal(word, location)
            else:
                return self.validate_word_vertical(word, location)   
         
    def put_words_board(self, word, location, orientation):
        utils = Utils()
        list_word = utils.word_to_tiles(word)
        row = location[0]
        column = location[1]
        i = 0
        for _ in list_word:
            self.grid[row][column].letter = list_word[i]
            self.grid[row][column].desactive_cell()
            row, column = utils.increment_coordinates(orientation, row, column)
            i += 1
    
    def find_cells_around_word(self, word, location, orientation, adjacent_cells):
        utils2 = ScrabbleUtils()
        if orientation == "H":
            utils2.cells_around_horizontal_word(word, location, adjacent_cells)
        elif orientation == "V":
            utils2.cells_around_vertical_word(word, location, adjacent_cells)
    
    def find_tiles_around_word(self, orientation, adjacent_tiles, board):
        utils = Utils()
        utils2 = ScrabbleUtils()
        if orientation == "H":
            adjacent_tiles = utils.remove_duplicate_columns(adjacent_tiles)
            return utils2.find_words_in_specific_direction(adjacent_tiles, 'H', board)
        elif orientation == "V":
            adjacent_tiles = utils.remove_duplicate_rows(adjacent_tiles)
            return utils2.find_words_in_specific_direction(adjacent_tiles, 'V', board)
        
###################################################################################################
    def validate_adjacent_words(self, word_in_validation, other_words):
        board2 = Board()
        original_word = word_in_validation[0]
        original_location = word_in_validation[1]
        original_orientation = word_in_validation[2]
        adjacent_cells = []
        adjacent_tiles = []
        for list in other_words:
            another_word = list[0]
            another_location = list[1]
            another_orientation = list[2]
            board2.put_words_board(another_word, another_location, another_orientation)
        board2.put_words_board(original_word, original_location, original_orientation)
        self.find_cells_around_word(original_word, original_location, original_orientation, adjacent_cells)
        if ScrabbleUtils().are_cells_around_word_valid(adjacent_cells, adjacent_tiles, board2):
            word = self.find_tiles_around_word(original_orientation, adjacent_tiles, board2)
            return word

    def verify_word_and_adjacents(self, word, location, orientation, residual_words=[]):
        board = self
        adjacent_cells = []
        adjacent_tiles = []
        utils = Utils()
        utils2 = ScrabbleUtils()
        dict = Dictionary()
        word_in_validation = [word, location, orientation]
        self.find_cells_around_word(word, location, orientation, adjacent_cells)
        if utils2.are_cells_around_word_valid(adjacent_cells, adjacent_tiles, board) is True:
            words_to_validate_without_word = self.find_tiles_around_word(orientation, adjacent_tiles, board)
            words_to_validate_with_word = self.validate_adjacent_words(word_in_validation, words_to_validate_without_word)
            real_words_to_validate_without_word = utils.convert_result_to_list_of_words(words_to_validate_without_word)
            real_words_to_validate_with_word = utils.convert_result_to_list_of_words(words_to_validate_with_word)
            new_words = set(real_words_to_validate_with_word) - set(real_words_to_validate_without_word)
            residual_words.extend(list(new_words))
            return dict.verify_word_list(real_words_to_validate_with_word)
        else:
            if self.is_empty() is True:
                return self.word_in_the_center(word, location, orientation)
