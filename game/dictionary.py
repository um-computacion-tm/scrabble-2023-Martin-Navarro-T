# dictionary.py 	

class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as file:
            self.all_words = set(word.strip().lower() for word in file)
            
    def remove_accents(self, word):
        word = word.lower()
        accents_dict = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u','ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u'}
        cleaned_word = ''.join(accents_dict.get(char, char) for char in word)
        return cleaned_word
    
    def verify_word(self,word):
        word = word.lower()
        return word in self.all_words
    
    def verify_word_list(self, word_list):
        for word in word_list:
            if not self.verify_word(word):
                return False
        return True