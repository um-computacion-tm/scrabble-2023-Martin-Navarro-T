import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile
from game.board import Board
from game.cell import Cell


    
class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertEqual(scrabble_game.current_turn, 0)

    def test_playing(self):
        game = ScrabbleGame(players_count=2)
        self.assertTrue(game.playing())

    def test_next_turn(self):
        game = ScrabbleGame(players_count=3)
        current_turn = game.current_turn
        game.next_turn()
        self.assertEqual(game.current_turn, current_turn + 1)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[1].name)

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)

if __name__ == '__main__':
    unittest.main()
##################################################################
'''
    def setUp(self):
        self.game = ScrabbleGame(2)  # Crea una instancia de ScrabbleGame con 2 jugadores
        self.player = self.game.players[0]  # Obtiene el primer jugador como jugador actual
        self.game.current_player = self.player  # Establece el jugador actual en el juego

        # Configura las letras disponibles para el jugador 1
        self.player.tiles = ["c", "a", "b", "x", "y"]


    def test_validate_word(self):
        # Caso 1: Palabra válida y se puede colocar en el tablero
        self.player.tiles = ["c", "a", "b", "x", "y"]  # Letras disponibles para el jugador
        self.assertTrue(self.game.validate_word("cab", (0, 0), "h"))

        # Caso 2: Palabra no válida porque el jugador no tiene las letras necesarias
        self.player.tiles = ["a", "b", "c", "d", "e"]  # Letras disponibles para el jugador
        self.assertFalse(self.game.validate_word("dog", (0, 0), "h"))

        # Caso 3: Palabra no válida porque no cabe en el tablero
        self.player.tiles = ["c", "a", "b", "x", "y"]  # Letras disponibles para el jugador
        self.assertFalse(self.game.validate_word("table", (0, 0), "v"))

        # Caso 4: Palabra válida pero no tiene suficientes letras en el rack
        self.player.tiles = ["c", "a", "b"]  # Letras disponibles para el jugador
        self.assertFalse(self.game.validate_word("cabby", (0, 0), "h"))

        # Caso 5: Palabra válida y se puede colocar en el tablero (otra ubicación)
        self.player.tiles = ["c", "a", "b", "x", "y"]  # Letras disponibles para el jugador
        self.assertTrue(self.game.validate_word("cab", (5, 5), "v"))

        # Caso 6: Palabra no válida porque no cabe en el tablero (ubicación incorrecta)
        self.player.tiles = ["c", "a", "b", "x", "y"]  # Letras disponibles para el jugador
        self.assertFalse(self.game.validate_word("cabbage", (0, 0), "h"))

        # Caso 7: Palabra válida pero el jugador no tiene todas las letras necesarias
        self.player.tiles = ["c", "a", "b"]  # Letras disponibles para el jugador
        self.assertFalse(self.game.validate_word("cabby", (0, 0), "h"))
'''



