#test_main.py
from main import Main
import unittest
from unittest.mock import patch
from io import StringIO
import io
import sys
from game.cell import Cell
from unittest.mock import call

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

    @patch('builtins.input', side_effect=['3']) 
    def test_player_count_input_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)
    
    @patch('builtins.input', side_effect=['5', '3'])
    def test_player_count_input_invalid_then_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('Valor inválido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)
    
    @patch('builtins.input', side_effect=['2'])
    def test_next_turn_main(self, mock_input):
        main = Main()
        self.assertEqual(main.game.turn, 0)
        main.next_turn()
        self.assertEqual(main.game.turn, 1)

if __name__ == "__main__":
    unittest.main()

