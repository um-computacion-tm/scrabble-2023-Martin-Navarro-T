#main.py 
import os
import sys

# Ruta absoluta del directorio raíz del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))
# Agregar el directorio raíz a sys.path
sys.path.insert(0, project_root)
# Importar las clases de game sin problemas
from game.scrabble import ScrabbleGame, InvalidJokerConversion

class Main:
    def __init__(self):
        print('Bienvenido a Scrabble Game!')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)  
        self.board = self.game.get_board()
        
    def valid_player_count(self, player_count):
        try:
            count = int(player_count)
            return 2 <= count <= 4
        except ValueError:
            return False
    
    def get_player_count(self):
        while True:
            player_count = input('Cantidad de jugadores (2-4): ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor inválido. Debe ser un número entre 2 y 4')
    
    def next_turn(self):
        self.game.next_turn()

    def show_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.game.current_player.rack)
    
    def take_turn(self):
        print(f'Tu mano actual es: {self.show_rack()}')
        while True:
            option = input("Elija alguna opción:\n1) Jugar\n2) Ver Puntuación\n3) Pasar")
            option = self.game.input_to_int(option)
            if option == 1:
                self.play()
                break
            elif option == 2:
                self.show_scores()
            elif option == 3:
                break
              
if __name__ == '__main__':
    main = Main()