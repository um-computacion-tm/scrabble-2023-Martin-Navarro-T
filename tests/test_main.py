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
from game.scrabble import ScrabbleGame
from unittest.mock import patch


class TestMain(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['2', 'marta', 'martin'])   
    def test_valid_player_count(self,mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3','marta', 'martin', 'ian'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)

    @patch('builtins.input', side_effect=['2','marta', 'martin'])
    def test_next_turn_main(self, mock_input):
        main = Main()
        self.assertEqual(main.game.turn, 0)
        main.game.next_turn()
        self.assertEqual(main.game.turn, 1)

    def test_take_turn(self):
        with patch('builtins.print') as mock_print, \
             patch('builtins.input', side_effect=['2','marta', 'martin', 'foo', '3', '2']) as mock_input:
            main = Main()
            main.game.next_turn()
            main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
            main.game.current_player.score = 16
            main.take_turn()
            expected_output = [
                call("------------------------------------------------------------------------------------------"),
                call('Bienvenido a Scrabble Game!'),
                call('------------------------------------------------------------------------------------------'),
                call('------------------------------------------------------------------------------------------'),
                call('Cantidad de Jugadores: 2 '),
                call('------------------------------------------------------------------------------------------'),
                call('------------------------------------------------------------------------------------------'),
                call('Hola Marta!'),
                call('------------------------------------------------------------------------------------------'),
                call('------------------------------------------------------------------------------------------'),
                call('Hola Martin!'),
                call('------------------------------------------------------------------------------------------'),]
                #call('Tu mano actual es: [A] [B]')]
            mock_print.assert_has_calls(expected_output, any_order=False)

    @patch('builtins.input', side_effect=['2','marta', 'martin', '1', '2'])
    def test_convert_tiles_in_another_tile(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(2, numbers)
        self.assertEqual(len(main.game.players[0].rack), 4)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin', 'd', '0'])
    def test_convert_tiles_in_another_tile_wrong(self, mock_input, mock_print):
        main = Main()
        numbers = [1, 2, 3, 4, 5, 6, 7]
        main.convert_tiles_in_another_tile(4, numbers)
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 2 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('El valor ingresado es invalido, porfavor intente de nuevo'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------')]
        mock_print.assert_has_calls(expected_output, any_order=False)
        
    @patch('builtins.input', side_effect=['2','marta', 'martin', '2', '1', '3'])
    def test_exchange_tiles(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 4)
    

    @patch('builtins.input', side_effect=['2','marta', 'martin', '1', '0'])
    def test_exchange_tiles_initial_limit_index(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O',1), Tile('L',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 7)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin','d', '0'])
    def test_exchange_tiles_exit(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.exchange_tiles()
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 2 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('El valor ingresado es invalido, porfavor intente de nuevo'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------')]

        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin', 'A', '0'])
    def test_change_joker_exception(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('B', 1)]
        main.change_joker_to_tile()
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 2 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Se ha cambiado la letra por el comodin'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Error: No tienes un comodin en tu rack'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------')]


        mock_print.assert_has_calls(expected_output, any_order=False)
        

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin', 'AB', 'A'])
    def test_change_joker_to_tile_second_try(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('?', 0), Tile('B', 1)]
        main.change_joker_to_tile()
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 2 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('El valor ingresado es invalido, porfavor intente de nuevo'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Se ha cambiado la letra por el comodin'),
            call('------------------------------------------------------------------------------------------')]

        mock_print.assert_has_calls(expected_output, any_order=False)
        
    @patch('builtins.input', side_effect=['2','marta', 'martin', '1', '7'])
    def test_exchange_tiles_final_limit_index(self, mock_input):
        main = Main()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1), Tile('H', 4), Tile('O',1), Tile('L',1)]
        main.game.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 7)
        
        
    @patch('builtins.input', side_effect=['2','marta', 'martin', 'A'])
    def test_change_joker_to_tile_true(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('?', 0), Tile('B', 1)]
        main.change_joker_to_tile()
        self.assertEqual(main.game.current_player.rack[0].letter, 'A' )
        
    @patch('builtins.input', side_effect=['2','marta', 'martin', 'hola', '7', '7', 'H']) #Horizontal
    def test_get_word_location_orientation(self, mock_input):
        main = Main()
        word, location, orientation = main.get_word_location_orientation()
        self.assertEqual(word, 'HOLA')
        self.assertEqual(location, (7,7))
        self.assertEqual(orientation, 'H') #Horizontal

    @patch('builtins.input', side_effect=['2','marta', 'martin', '0'])
    def test_get_word_location_orientation_return(self, mock_input):
        main = Main()
        word, location, orientation = main.get_word_location_orientation()
        self.assertEqual(word, '0')
        self.assertEqual(location, None)
        self.assertEqual(orientation, None)   



    
    @patch.object(Main, 'get_word_location_orientation', return_value=('0', None, None))
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin', '0'])
    def test_placed_word_break(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        main.place_word()

    @patch.object(Main, 'get_word_location_orientation', return_value=('hola', (6,6), 'H')) #Horizontal
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2','marta', 'martin', '0',])
    def test_placed_word_exception(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.place_word()
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 2 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('Error: Su palabra no se cruza con ninguna palabra valida'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------')]

        mock_print.assert_has_calls(expected_output, any_order=False)

    @patch('builtins.input', side_effect=['2','marta', 'martin'])
    def test_get_tiles_to_full_rack(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
        self.assertEqual(len(main.game.current_player.rack), 2)
        main.get_tiles_to_full_rack()
        self.assertEqual(len(main.game.current_player.rack), 7)
    
    @patch('builtins.input', side_effect=['2','marta', 'martin'])
    def test_get_tiles_to_full_rack_with_7_tiles_in_rack(self, mock_input):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1), Tile('A', 1), Tile('B', 1), Tile('A', 1), Tile('B', 1), Tile('C', 1)]
        self.assertEqual(len(main.game.current_player.rack), 7)
        main.get_tiles_to_full_rack()
        self.assertEqual(len(main.game.current_player.rack), 7)


        
    
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3','marta', 'martin', 'ian', '2', '3'])
    def test_take_turn_show_scores_and_pass_turn(self, mock_input, mock_print):
        main = Main()
        main.game.next_turn()
        main.game.current_player.rack = [Tile('A', 1), Tile('B', 1)]
        main.game.current_player.score = 16
        main.take_turn()
        expected_output = [
            call("------------------------------------------------------------------------------------------"),
            call('Bienvenido a Scrabble Game!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Cantidad de Jugadores: 3 '),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Marta!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Martin!'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Hola Ian!'),
            call('------------------------------------------------------------------------------------------'),
            call('Tus fichas para jugar son: [A] [B]'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('Puntuación de los jugadores:'),
            call('El jugador 1: Marta, tiene una puntuación de: 16'),
            call('El jugador 2: Martin, tiene una puntuación de: 0'),
            call('El jugador 3: Ian, tiene una puntuación de: 0'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------'),
            call('------------------------------------------------------------------------------------------')]




        mock_print.assert_has_calls(expected_output, any_order=False)
    
    @patch.object(Main, 'play', return_value=('hola', (7,7), 'H')) #Horizontal
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3','marta', 'martin', 'ian', '1'])
    def test_take_turn_player_play(self, mock_input, mock_print, mock_object):
        main = Main()
        main.game.next_turn()
        player = main.game.current_player
        player.rack = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        main.take_turn()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['4','marta', 'martin', 'ian', 'rey'])
    def test_show_scores(self, mock_input, mock_print):
        main = Main()
        main.game.players[0].score = 90
        main.game.players[1].score = 172
        main.game.players[2].score = 78
        main.game.players[3].score = 134
        main.show_scores()
        expected_output = [
        call('Bienvenido a Scrabble Game!'),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Cantidad de Jugadores: 4 '),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Hola Marta!'),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Hola Martin!'),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Hola Ian!'),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Hola Rey!'),
        call('------------------------------------------------------------------------------------------'),
        call('------------------------------------------------------------------------------------------'),
        call('Puntuación de los jugadores:'),
        call('El jugador 2: Martin, tiene una puntuación de: 172'),
        call('El jugador 4: Rey, tiene una puntuación de: 134'),
        call('El jugador 1: Marta, tiene una puntuación de: 90'),
        call('El jugador 3: Ian, tiene una puntuación de: 78'),
        call('------------------------------------------------------------------------------------------')]


        mock_print.assert_has_calls(expected_output, any_order=False)



        
@patch.object(ScrabbleGame, 'get_current_player_id', return_value=1)
@patch('builtins.print')
@patch('builtins.input', side_effect=['2', 'Martin', 'Gato', '0'])
def test_play_game(self, mock_input, mock_print, mock_get_current_player_id):
    main = Main()
    main.play_scrabble_game()
    
    @patch.object(Main, 'put_initial_tiles_bag')
    @patch.object(Main, 'put_tiles_in_rack')
    @patch.object(Main, 'game_over', side_effect=[False, True])
    @patch.object(Main, 'next_turn')
    @patch.object(Main, 'get_current_player_id', return_value=(1))
    @patch.object(Main, 'show_board')
    @patch.object(Main, 'take_turn', return_value=('2'))
    @patch.object(Main, 'get_tiles_to_full_rack')
    @patch.object(Main, 'show_scores')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', 'Martin', 'Gato', '0'])
    
    def test_play_game2(self, mock_input, mock_print, mock_show_scores, mock_get_tiles_to_full_rack, mock_take_turn, mock_get_current_player_id, mock_next_turn, mock_game_over, mock_put_tiles_in_rack, mock_put_initial_tiles_bag):
        main = Main()
        main.play_scrabble_game()
        


if __name__ == '__main__':
    unittest.main()