# cell.py
from game.models import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter: Tile): #agregado
        if self.letter is None:
            self.letter = letter
            return True

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def remove_letter(self): #nuevo
        removed_letter = self.letter
        self.letter = None
        return removed_letter
