#tile.py

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def get_value_by_letter(self, letter):
        return self.value if self.letter == letter else 0
