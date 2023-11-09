#tile.py

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        
    def convert_tile(self, new_letter, new_value):
        self.letter = new_letter
        self.value = new_value
        
    def is_joker(self):
        if self.value == 0:
            return True
        return False

    def __repr__(self):
        return (self.letter)