# board.py
from game.cell import Cell
from game.tile import Tile

class Board:
    def __init__(self):
        self.size = 15  # Establece el tamaño del tablero
        self.grid = [
            [Cell(1, '') for _ in range(self.size)]
            for _ in range(self.size)
        ]

    def place_tile(self, location_x, location_y, tile):
        if 0 <= location_x < 15 and 0 <= location_y < 15:
            cell = self.grid[location_x][location_y]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False
    
    def validate_word(self, start_location_x, start_location_y, word, orientation):
        for i, letter in enumerate(word):
            if orientation == 'H':
                location_x = start_location_x
                location_y = start_location_y + i
            elif orientation == 'V':
                location_x = start_location_x + i
                location_y = start_location_y

            if location_x >= 15 or location_y >= 15 or (self.grid[location_x][location_y].letter is None or self.grid[location_x][location_y].letter.letter != letter):
                return False
        return True

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location
        word_length = len(word)

        if orientation == "H":
            return col + word_length <= 15
        elif orientation == "V":
            return row + word_length <= 15

    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)
