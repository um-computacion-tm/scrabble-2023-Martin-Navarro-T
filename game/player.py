# player.py
class Player:
    def __init__(self, name, bag_tiles=None):
        self.name = name
        self.tiles = []
        self.score = 0
        self.is_current_turn = False
        self.bag_tiles = bag_tiles
        self.played_words = []  # Lista para llevar un registro de las palabras jugadas

    def draw_tiles(self, bag_tiles, count):
        new_tiles = bag_tiles.take(count)
        self.tiles.extend(new_tiles)

    def exchange_tiles(self, bag_tiles, tiles_to_exchange):
        tiles_to_keep = [tile for tile in self.tiles if tile not in tiles_to_exchange]
        tiles_taken = bag_tiles.take(len(tiles_to_exchange))

        bag_tiles.put(tiles_to_exchange)
        self.tiles = tiles_to_keep + tiles_taken

    def view_tiles(self):
        return self.tiles[:]

    def view_score(self):
        return self.score

    def start_turn(self):
        self.is_current_turn = True

    def end_turn(self):
        self.is_current_turn = False

    def pass_turn(self):
        self.end_turn()

    def check_tile_in_hand(self, tile):
        return tile in self.tiles

    def get_hand_size(self):
        return len(self.tiles)

    def get_score(self):
        total_score = 0
        for cell in self.board.played_cells:
            total_score += cell.calculate_value()
        return total_score

    def validate_word(self, word):
        word_letters = list(word)
        rack_letters = [tile.letter for tile in self.tiles]

        for letter in word_letters:
            if letter not in rack_letters:
                return False
            rack_letters.remove(letter)

        return True
