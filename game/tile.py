#tile.py
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        
    def get_value_by_letter(self, letter):
        return self.value if self.letter == letter else 0
        
    def is_joker(self):
        if self.value == 0:
            return True
        else:
            return False
        
    def test_is_joker(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_joker(), True)
        
    def convert_tile(self, new_letter, new_value):
        self.letter = new_letter
        self.value = new_value