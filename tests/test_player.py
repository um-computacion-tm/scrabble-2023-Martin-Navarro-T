import unittest
from unittest.mock import Mock, patch
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile
from game.board import Board
from game.cell import Cell

class MockBoard:
    def __init__(self):
        self.grid = [[MockCell() for _ in range(15)] for _ in range(15)]

class MockCell:
    def __init__(self):
        self.letter = None
        self.multiplier = 1
        self.multiplier_type = ''

    def add_letter(self, letter):
        self.letter = letter

    def calculate_value(self):
        return self.letter.value if self.letter is not None else 0

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(name='Player 1')
        self.assertEqual(len(player_1.tiles), 0)
        self.assertEqual(player_1.score, 0)
        self.assertFalse(player_1.is_current_turn)
        self.assertEqual(player_1.name, 'Player 1')

    def test_draw_tiles(self):
        player = Player(name='Player 1')
        bag_tiles = BagTiles()

        player.draw_tiles(bag_tiles, 5)
        self.assertEqual(len(player.tiles), 5)

    def test_exchange_tiles(self):
        player = Player(name='Player 1')
        bag_tiles = BagTiles()
        
        player.draw_tiles(bag_tiles, 5)

        bag_tiles_count_before = len(bag_tiles.tiles)
        tiles_to_exchange = player.tiles[:2]  
        tiles_count_before = len(player.tiles)

        player.exchange_tiles(bag_tiles, tiles_to_exchange)
        self.assertEqual(len(player.tiles), tiles_count_before - 2 + len(tiles_to_exchange)) 
        self.assertEqual(len(bag_tiles.tiles), bag_tiles_count_before)
        
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
    
    def test_view_tiles(self):
        player = Player(name='Player 1')
        player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        tiles = player.view_tiles()
        self.assertEqual(tiles, player.tiles)

    def test_view_score(self):
        player = Player(name='Player 1')
        player.score = 15
        score = player.view_score()
        self.assertEqual(score, player.score)

    def test_start_end_turn(self):
        player = Player(name='Player 1')
        
        player.start_turn()
        self.assertTrue(player.is_current_turn)
        
        player.end_turn()
        self.assertFalse(player.is_current_turn)

    def test_pass_turn(self):
        self.player = Player("Player1")
        self.assertFalse(self.player.is_current_turn)  # Aseguramos que el turno no esté activo inicialmente
        self.player.start_turn()  # Activamos el turno
        self.assertTrue(self.player.is_current_turn)  # Verificamos que el turno esté activo
        self.player.pass_turn()  # Pasamos el turno
        self.assertFalse(self.player.is_current_turn)  # Verificamos que el turno ya no esté activo

    def test_check_tile_in_hand(self):
        self.player = Player("Player1")
        self.player.tiles = ['A', 'B', 'C']
        self.assertTrue(self.player.check_tile_in_hand('A'))
        self.assertTrue(self.player.check_tile_in_hand('B'))
        self.assertTrue(self.player.check_tile_in_hand('C'))
        self.assertFalse(self.player.check_tile_in_hand('D'))
        self.assertFalse(self.player.check_tile_in_hand('Z'))

    def test_get_hand_size(self):
        self.player = Player("Player1")
        self.player.tiles = ['A', 'B', 'C']
        self.assertEqual(self.player.get_hand_size(), 3)
    
    
    def test_get_score_no_played_cells(self):
        player = Player('Charlie')
        player.board = Mock()  # Crea un objeto Mock para simular el tablero
        player.board.played_cells = []  # Simula que no hay celdas jugadas
        self.assertEqual(player.get_score(), 0)

    def test_get_score_with_played_cells(self):
        player = Player('Charlie')
        player.board = Mock()  # Crea un objeto Mock para simular el tablero
        mock_cell_1 = MockCell(3)
        mock_cell_2 = MockCell(2)
        player.board.played_cells = [mock_cell_1, mock_cell_2]
        self.assertEqual(player.get_score(), 5)  # Total calculado: 3 + 2 = 5
    
    def test_validate_word_valid(self):
        player = Player('David')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertTrue(player.validate_word('ABC'))


    def test_validate_word_invalid(self):
        player = Player('Eve')
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 2)]
        self.assertFalse(player.validate_word('ABCD')) 
    
    def test_set_tiles(self):
        # Crear una instancia de Player
        player = Player(name="Jugador 1", bag_tiles=None)

        # Establecer las letras disponibles para el jugador
        tiles = ["a", "b", "c", "d", "e"]
        player.set_tiles(tiles)

        # Verificar que las letras se hayan establecido correctamente
        self.assertEqual(player.get_tiles(), tiles)

    def test_get_tiles(self):
        # Crear una instancia de Player
        player = Player(name="Jugador 1", bag_tiles=None)

        # Establecer las letras disponibles para el jugador
        tiles = ["a", "b", "c", "d", "e"]
        player.set_tiles(tiles)

        # Obtener las letras y verificar que coincidan con las establecidas
        self.assertEqual(player.get_tiles(), tiles)
class MockCell:
    def __init__(self, value):
        self.value = value

    def calculate_value(self):
        return self.value

if __name__ == "__main__":
    unittest.main()
