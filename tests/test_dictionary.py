import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_simple_verify(self):
        dic = Dictionary()
        word = "Hola"
        self.assertEqual(dic.verify_word(word), True)
    def test_remove_accents(self):
        dic = Dictionary()
        word = 'imaginación'
        self.assertEqual(dic.remove_accents(word), 'imaginacion')
    def test_remove_dieresis(self):
        dic = Dictionary()
        word = 'pingüino'
        self.assertEqual(dic.remove_accents(word), 'pinguino')
    def test_dont_remove_ñ(self):
        dic = Dictionary()
        word = 'piñón'
        self.assertEqual(dic.remove_accents(word), 'piñon')
    def test_verify_false_word(self):
        dic = Dictionary()
        word = "Kadabra"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_without_accents(self):
        dic = Dictionary()
        word = "Imaginacion"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Pingüino"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_without_dieresis(self):
        dic = Dictionary()
        word = "Pinguino"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_list_True(self):
        dic = Dictionary()
        word_list = ['Pato', 'Columna', 'Televisor']
        self.assertEqual(dic.verify_word_list(word_list), True)
    def test_verify_word_list_False(self):
        dic = Dictionary()
        word_list = ['Pato', 'Columna', 'Kalamacha']
        self.assertEqual(dic.verify_word_list(word_list), False)
