#cell.py
from game.tile import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None, status='active'):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.status = status
        self.original_state = {'multiplier': multiplier, 'multiplier_type': multiplier_type, 'letter': letter, 'status': 'active'}
    
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
        
    def add_letter(self,letter:Tile): 
        self.letter = letter
    
    def remove_letter(self): 
        removed_letter = self.letter
        self.letter = None
        return removed_letter
    
    def calculate_value_letter_and_word(self): 
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        if self.multiplier_type == 'word':
            return self.letter.value
    
    def desactive_cell(self): 
        self.status = 'desactive'
    
    def reset_cell(self): 
        self.letter = self.original_state.get('letter')
        self.status = self.original_state.get('status')
        self.multiplier = self.original_state.get('multiplier')
        self.multiplier_type = self.original_state.get('multiplier_type')
    
