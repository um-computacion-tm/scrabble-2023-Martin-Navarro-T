# dictionary.py 	
class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as file:
            self.dictionary = set(word.strip().lower() for word in file)
    def verify_word(self,word):
        word = word.lower()
        return word in self.dictionary
'''
import unicodedata

with open('dictionary.txt', 'r', encoding='utf-8') as file:
    word_list = set(word.strip().lower() for word in file)

class Dictionary:
    def remove_accents(self,word):
        word = ''.join(x for x in unicodedata.normalize('NFKD', word) if not unicodedata.combining(x))
        return word
    def verify_word(self,word):
        word = word.lower()
        return word in word_list
'''

'''
import os

class Dictionary:
    def __init__(self, file_path=None):
        # Si no se proporciona una ruta de archivo, usar la ruta completa
        if file_path is None:
            file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dictionary.txt")

        self.file_path = file_path
        self.words = set()
        self.load_dictionary()

    def load_dictionary(self):
        try:
            with open(self.file_path, "r") as file:
                self.words = set(word.strip().lower() for word in file)
        except FileNotFoundError:
            # print(f"El archivo de diccionario '{self.file_path}' no se encontró.")
            self.words = set()

    def is_valid_word(self, word):
        return word.lower() in self.words
'''
