# board.py
from game.cell import Cell
from game.models import Tile

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

    def validate_word(self, start_location_x, start_location_y, word, direction):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                location_y = start_location_y + i
                if location_y >= 15 or (self.grid[start_location_x][location_y].letter is None or self.grid[start_location_x][location_y].letter.letter != letter):
                    return False
            return True
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                location_x = start_location_x + i
                if location_x >= 15 or (self.grid[location_x][start_location_y].letter is None or self.grid[location_x][start_location_y].letter.letter != letter):
                    return False
            return True
        