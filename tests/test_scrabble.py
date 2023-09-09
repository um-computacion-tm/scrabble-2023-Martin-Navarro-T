import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertEqual(scrabble_game.current_turn, 0)

    def test_playing(self):
        # Crear un juego de Scrabble con 2 jugadores
        game = ScrabbleGame(players_count=2)
        # Verificar que el juego está en curso (playing)
        self.assertTrue(game.playing())

    def test_next_turn(self):
        # Crear un juego de Scrabble con 3 jugadores
        game = ScrabbleGame(players_count=3)
        # Obtener el turno actual antes de llamar a next_turn
        current_turn = game.current_turn
        # Llamar al método next_turn
        game.next_turn()
        # Verificar que el turno actual haya aumentado en 1
        self.assertEqual(game.current_turn, current_turn + 1)

    def test_next_turn_when_game_is_starting(self):
        # Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)  # Comparar nombres de jugadores

    def test_next_turn_when_player_is_not_the_first(self):
        # Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[1].name)  # Comparar nombres de jugadores

    def test_next_turn_when_player_is_last(self):
        # Suponiendo que tenemos 3 jugadores, luego del jugador 2, le toca al jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)  # Comparar nombres de jugadores
    
if __name__ == '__main__':
    unittest.main()
