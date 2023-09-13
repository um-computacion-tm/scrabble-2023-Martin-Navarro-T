# cell.py
from game.tile import Tile
from typing import List

class Cell:
    def __init__(self, multiplier=1, multiplier_type="", letter=None, active=True, value=0): #multiplier, multiplier_type, letter
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active
        self.value = value

    def add_letter(self, letter: Tile): 
        if self.letter is None:
            self.letter = letter
            return True

    def remove_letter(self): 
        removed_letter = self.letter
        self.letter = None
        return removed_letter
        
    def add_player_starting_position(self, player):
        self.is_starting_position = True
        self.player_starting_position = player

    def is_empty(self):
        return self.letter is None

    def has_letter(self, letter):
        return self.letter and self.letter.letter == letter

    def apply_word_multiplier(self, word_multiplier):
        if self.multiplier_type == 'word':
            self.multiplier *= word_multiplier

    def apply_letter_multiplier(self, letter_multiplier):
        if self.multiplier_type == 'letter':
            self.multiplier *= letter_multiplier
    
    def calculate_value(self):
        if not self.active:
            return 0
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
class Calculate_value:
    @staticmethod
    def calculate_word_value(cells: List[Cell]) -> int:
        total_value = 0
        word_multiplier = 1

        for cell in cells:
            if cell.active:
                cell_value = Calculate_value.calculate_cell_value(cell)
                word_multiplier *= Calculate_value.calculate_word_multiplier(cell)
                total_value += cell_value

        return total_value * word_multiplier

    @staticmethod
    def calculate_cell_value(cell: Cell) -> int:
        if cell.letter is not None:
            if cell.multiplier_type == 'letter':
                return cell.letter.value * cell.multiplier
            else:
                return cell.letter.value
        else:
            return 0  # Celda vacía

    @staticmethod
    def calculate_word_multiplier(cell: Cell) -> int:
        if cell.multiplier_type == 'word':
            return cell.multiplier
        else:
            return 1

