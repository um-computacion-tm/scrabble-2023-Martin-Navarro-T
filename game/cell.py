# cell.py
from game.models import Tile
from typing import List

class Cell:
    def __init__(self, multiplier=1, multiplier_type="", letter=None): #multiplier, multiplier_type, letter
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = True

    def add_letter(self, letter: Tile): 
        if self.letter is None:
            self.letter = letter
            return True

    def remove_letter(self): 
        removed_letter = self.letter
        self.letter = None
        return removed_letter
    
    def calculate_value(self):
        if not self.active:  # Si la celda no está activa, su valor es 0
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
                cell_value = cell.calculate_value()
                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier  
                total_value += cell_value

        return total_value * word_multiplier  
