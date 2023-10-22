#test_main.py
from main import Main
import unittest
from unittest.mock import patch
from io import StringIO
import io
import sys
from game.cell import Cell
from unittest.mock import call
from game.tile import Tile


class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['3'])   
    def test_valid_player_count(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)

    @patch('builtins.input', side_effect=['2'])
    def test_next_turn_main(self, mock_input):
        main = Main()
        self.assertEqual(main.game.turn, 0)
        main.next_turn()
        self.assertEqual(main.game.turn, 1)

    def test_take_turn(self):
        with patch('builtins.print') as mock_print, \
             patch('builtins.input', side_effect=['2', 'foo', '3', '2']) as mock_input:
            main = Main()
            main.game.next_turn()
            main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
            main.game.current_player.score = 16
            main.take_turn()
            expected_output = [
                call('Bienvenido a Scrabble Game!'),
                call('Tu mano actual es: [A] [B]'),
            ]
            mock_print.assert_has_calls(expected_output, any_order=False)

    @patch('builtins.input', side_effect=['2', '1', '2'])
    def test_convert_tiles_in_another_tile(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(2, numbers)
        self.assertEqual(len(main.game.players[0].rack), 4)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'd', '0'])
    def test_convert_tiles_in_another_tile_wrong(self, mock_input, mock_print):
        main = Main()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(4, numbers)
        expected_output = [
            call('Bienvenido a Scrabble Game!'),
            call('Valor invalido, intente de nuevo'),]
        mock_print.assert_has_calls(expected_output, any_order=False)
        
    @patch('builtins.input', side_effect=['2', '2', '1', '3'])
    def test_exchange_tiles(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 4)
    

    @patch('builtins.input', side_effect=['2', '1', '0'])
    def test_exchange_tiles_initial_limit_index(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O',1), Tile('L',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 7)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'd', '0'])
    def test_exchange_tiles_exit(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.exchange_tiles()
        expected_output = [
            call('Bienvenido a Scrabble Game!'),
            call('Valor invalido, intente de nuevo'),
        ]
        mock_print.assert_has_calls(expected_output, any_order=False)
    
if __name__ == '__main__':
    unittest.main()


