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


if __name__ == '__main__':
    unittest.main()


