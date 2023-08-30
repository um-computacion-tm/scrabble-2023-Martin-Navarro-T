# player.py
class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.score = 0
        self.is_current_turn = False

    def draw_tiles(self, bag_tiles, count):
        new_tiles = bag_tiles.take(count)
        self.tiles.extend(new_tiles)

    def exchange_tiles(self, bag_tiles, tiles_to_exchange):
        tiles_to_keep = [tile for tile in self.tiles if tile not in tiles_to_exchange]
        tiles_taken = bag_tiles.take(len(tiles_to_exchange))
        
        bag_tiles.put(tiles_to_exchange)  
        self.tiles = tiles_to_keep + tiles_taken

    def calculate_score(self, cells):
        score = 0
        word_multiplier = 1

        for cell in cells:
            cell_score = 0

            if cell.letter is not None:
                cell_score = cell.calculate_value()

                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier
                elif cell.multiplier_type == 'letter':
                    cell_score *= cell.multiplier

            score += cell_score

        return score * word_multiplier


    def play_word(self, board, start_cell, word, direction):
        if not self.is_current_turn:
            return False #x

        cells_to_play = []  
        current_cell = start_cell

        for letter in word:
            if direction == 'horizontal':
                col = current_cell[1]
                cells_to_play.append((start_cell[0], col))
                current_cell = (current_cell[0], col + 1)
            else:
                current_cell = (current_cell[0] + 1, current_cell[1]) #x
                cells_to_play.append((current_cell[0], start_cell[1])) #x
                cell.add_letter(self.tiles.pop(0)) #x

        word_multiplier = 1
        for cell_row, cell_col in cells_to_play:
            cell = board.grid[cell_row][cell_col]
            if cell.letter is not None:
                return False #x
            cell.add_letter(self.tiles.pop(0))

        word_score = self.calculate_score([board.grid[row][col] for row, col in cells_to_play])
        self.score += word_score * word_multiplier

        self.is_current_turn = False
        return True

    def view_tiles(self):
        return self.tiles[:]

    def view_score(self):
        return self.score

    def start_turn(self):
        self.is_current_turn = True

    def end_turn(self):
        self.is_current_turn = False

