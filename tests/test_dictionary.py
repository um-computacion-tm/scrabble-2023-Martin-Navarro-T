import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_simple_verify(self):
        dic = Dictionary()
        word = "Hola"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_false_word(self):
        dic = Dictionary()
        word = "Kadabra"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Pingüino"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Pingüino"
        self.assertEqual(dic.verify_word(word), True)

'''
import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_remove_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.remove_accents(word), "Imaginacion")
    def test_simple_verify(self):
        dic = Dictionary()
        word = "Hola"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_false_word(self):
        dic = Dictionary()
        word = "Kadabra"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Imaginación"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Pingüino"
        self.assertEqual(dic.verify_word(word), True)
'''

'''
import unittest
from game.dictionary import Dictionary
from unittest.mock import mock_open, patch

class TestDictionary(unittest.TestCase):
    def test_is_valid_word_valid(self):
        # Verificar si una palabra válida está en el diccionario
        # Crear una instancia de Dictionary y agregar la palabra "apple"
        dictionary = Dictionary()
        dictionary.words.add("apple")
        valid_word = "apple"
        self.assertTrue(dictionary.is_valid_word(valid_word))

    def test_is_valid_word_invalid(self):
        # Verificar si una palabra inválida no está en el diccionario
        # Crear una instancia de Dictionary sin agregar la palabra "banana"
        dictionary = Dictionary()
        invalid_word = "banana"
        self.assertFalse(dictionary.is_valid_word(invalid_word))
        
    def test_load_dictionary_file_not_found(self):
        # Simula el FileNotFoundError al abrir el archivo "dictionary.txt"
        with patch("builtins.open", side_effect=FileNotFoundError()):
            dictionary = Dictionary(file_path="dictionary.txt")
            # Verifica que el conjunto de palabras esté vacío después de la excepción
            self.assertEqual(len(dictionary.words), 0)
            #print(f"Ruta del archivo: {dictionary.file_path}")
if __name__ == '__main__':
    unittest.main()
'''