import unittest
from game.scrabble import ScrabbleGame
from game.tile import Tile
from unittest.mock import patch

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
