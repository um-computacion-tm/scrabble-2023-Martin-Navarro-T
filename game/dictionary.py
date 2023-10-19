# dictionary.py 	
import unicodedata
class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as file:
            self.dictionary = set(word.strip().lower() for word in file)
            
    def verify_word(self,word):
        word = word.lower()
        return word in self.dictionary
    
    def remove_accents(self,word):
        word = ''.join(x for x in unicodedata.normalize('NFKD', word) if not unicodedata.combining(x))
        return word
