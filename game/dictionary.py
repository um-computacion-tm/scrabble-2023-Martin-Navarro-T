# dictionary.py 
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
