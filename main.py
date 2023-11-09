#main.py
from game.scrabble import ScrabbleGame, InvalidWordException, InvalidJokerConversion, InvalidRackException

class Main:
    def __init__(self):
        print("------------------------------------------------------------------------------------------")
        print('Bienvenido a Scrabble Game!')
        print("------------------------------------------------------------------------------------------")
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)  # Primero crea la instancia del juego. 
        self.board = self.game.get_board()
        self.players_names()  # Llama a la función después de crear el juego.
        
    def valid_player_count(self, player_count):
        try:
            count = int(player_count)
            return 2 <= count <= 4
        except ValueError:
            return False
    
    def get_player_count(self):
        while True:
            player_count = input('--> Porfavor ingrese la cantidad de jugadores (2-4): ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            
            print("------------------------------------------------------------------------------------------")
            print('Error: Solo pueden jugar de 2 a 4 jugadores, ingrese el numero de jugadores')
            print("------------------------------------------------------------------------------------------")
            
    def players_names(self):
        print("------------------------------------------------------------------------------------------") 
        print(f"Cantidad de Jugadores: {len(self.game.players)} ")
        print("------------------------------------------------------------------------------------------") 
        for i in range(len(self.game.players)):
            self.game.players[i].name = str(input(f"--> Ingrese el nombre del jugador {i}: "))
            print("------------------------------------------------------------------------------------------") 
            print(f"Hola {self.game.players[i].name.strip().title()}!")
            print("------------------------------------------------------------------------------------------") 
            
    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(len(self.board.grid))]))
        for row_index, row in enumerate(self.board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )

    def show_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.game.current_player.rack)
    
    def take_turn(self):
        print(f'Tus fichas para jugar son: {self.show_rack()}') 
        while True:
            print("------------------------------------------------------------------------------------------")
            option = input("Menú de opciones:\n1) Jugar\n2) Ver Puntuación\n3) Pasar\n--> Que opción elije?: ")
            print("------------------------------------------------------------------------------------------")
            option = self.game.input_to_int(option) #input_to_int
            if option == 1:
                self.play()
                break
            elif option == 2:
                self.show_scores()
            elif option == 3:
                break
    
    def play(self):
        options = {1: self.place_word, 2: self.reorganize, 3: self.exchange_tiles, 4: self.change_joker_to_tile, 5: self.quite_game }
        while True:
            print("------------------------------------------------------------------------------------------")
            option = input("Menú de opciones:\n1) Colocar Fichas\n2) Reorganizar Rack\n3) Cambiar Fichas\n4) Converir Comodin\n5) Pasar Turno\n--> Que opción elije?: ")
            print("------------------------------------------------------------------------------------------")
            option = self.game.input_to_int(option)
            option_function = options.get(option)
            if option_function is None:
                print("------------------------------------------------------------------------------------------")
                print('El valor ingresado es invalido, porfavor intente de nuevo')
                print("------------------------------------------------------------------------------------------")
            elif self.player_action(option_function):
                break

    def player_action(self, option_function):
        if option_function is not None:
            option_result = option_function()
            if option_result == 'finalizar': 
                return True

    def quite_game(self):
        return 'finalizar'
    
    def show_scores(self):
        sorted_players = sorted(self.game.players, key=lambda player: player.score, reverse=True)
        print("------------------------------------------------------------------------------------------")
        print("Puntuación de los jugadores:")
        for _, player in enumerate(sorted_players, start=1):
            print(f"El jugador {player.id}: {player.name.title()}, tiene una puntuación de: {player.score}")
        print("------------------------------------------------------------------------------------------")
    
    def place_word(self): 
        while True:
            try:
                word, location, orientation = self.get_word_location_orientation()
                if word == '0':
                    break
                self.validate_and_put_word(word, location, orientation)
                return 'finalizar'
            except (InvalidWordException, InvalidRackException) as e:
                print(f'Error: {e}')
                print("------------------------------------------------------------------------------------------")
                validate = input('Puedes volver apretando 0 o pulsa cualquier tecla para continuar: ')
                print("------------------------------------------------------------------------------------------")
                if validate == '0':
                    break
    
    def get_word_location_orientation(self):
        while True:
            word = input('--> Ingrese una palabra (0 para pasar): ')
            word = self.game.clean_word_to_use(word)
            if word == '0':
                return word, None, None
            print("------------------------------------------------------------------------------------------")
            location_x = input('--> Ingrese la fila en donde empezará (0-14): ')
            print("------------------------------------------------------------------------------------------")
            location_x = self.game.input_to_int(location_x)
            print("------------------------------------------------------------------------------------------")
            location_y = input('--> Ingrese la columna en donde empezará (0-14): ')
            print("------------------------------------------------------------------------------------------")
            location_y = self.game.input_to_int(location_y)
            print("------------------------------------------------------------------------------------------")
            location = (location_x, location_y)
            print("------------------------------------------------------------------------------------------")
            orientation = input('--> Ingrese la orientación [Vertical(V) o Horizontal(H)]: ')
            print("------------------------------------------------------------------------------------------")
            orientation = orientation.strip().upper()
            orientation = self.game.validate_orientation(orientation)
            return word, location, orientation
    
    def validate_and_put_word(self, word, location, orientation):
        if self.game.validate_word(word, location, orientation):
            self.game.deduct_tiles_from_player(word, location, orientation)
            self.game.calculate_and_update_score(word, location, orientation)
            self.game.put_word(word, location, orientation)
            

    def exchange_tiles(self):
        while True:
            print("------------------------------------------------------------------------------------------") 
            amount = input("--> ¿Cuántas fichas quieres intercambiar? (1-7) (0 para salir): ")
            print("------------------------------------------------------------------------------------------") 
            amount = self.game.input_to_int(amount)
            numbers = [1, 2, 3, 4, 5, 6, 7]
            if amount in numbers:
                self.convert_tiles_in_another_tile(amount, numbers)
                return 'finalizar'
            elif amount == 0:
                break
            else: 
                print("------------------------------------------------------------------------------------------") 
                print('El valor ingresado es invalido, porfavor intente de nuevo')
                print("------------------------------------------------------------------------------------------") 
    
    def convert_tiles_in_another_tile(self, amount, numbers):
        for i in range(amount):
            print("------------------------------------------------------------------------------------------") 
            index = input("--> Elige la ficha que vas a intercambiar una a una (1-7): ")
            print("------------------------------------------------------------------------------------------") 
            index = self.game.input_to_int(index)
            if index in numbers:
                self.game.current_player.exchange_tiles(index, self.game.bagtiles)
            elif index == 0:
                break
            else:
                print("------------------------------------------------------------------------------------------") 
                print('El valor ingresado es invalido, porfavor intente de nuevo')
                print("------------------------------------------------------------------------------------------") 
                
    #Opcion 3 de Play
    def change_joker_to_tile(self):
        while True:
            try:
                if self.convert_joker_into_tile():
                    break
            except InvalidJokerConversion as e:
                print("------------------------------------------------------------------------------------------") 
                print(f'Error: {e}')
                print("------------------------------------------------------------------------------------------") 

    def convert_joker_into_tile(self):
        print("------------------------------------------------------------------------------------------") 
        new_letter = input('--> Ingrese la letra que desea cambiar por el comodin (0 para terminar): ')
        print("------------------------------------------------------------------------------------------") 
        new_letter= new_letter.strip().upper()
        alphabet = ['A', 'B', 'C', 'CH', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
        if new_letter in alphabet:
            print("------------------------------------------------------------------------------------------") 
            print('Se ha cambiado la letra por el comodin')
            print("------------------------------------------------------------------------------------------") 
            self.game.convert_joker(new_letter)
            return True
        elif new_letter == '0':
            return True
        else:
            print("------------------------------------------------------------------------------------------") 
            print('El valor ingresado es invalido, porfavor intente de nuevo')
            print("------------------------------------------------------------------------------------------") 
            return False     
        
    def reorganize(self):
        while True:
            self.game.shuffle_rack()
            print(f'{self.show_rack()}')
            organize = input("Para continuar puedes apretar cualquier tecla(0 para terminar): ")
            organize = organize.strip().upper()
            if organize == "0":
                break
    
    def get_tiles_to_full_rack(self):
        amount_tiles_needed = 7 - len(self.game.current_player.rack)
        if amount_tiles_needed == 0:
            return
        elif amount_tiles_needed > 0:
            self.game.put_tiles_in_rack(amount_tiles_needed)

    def play_scrabble_game(self):
        print("------------------------------------------------------------------------------------------")
        print('Ha comenzado la Partida de Scrabble Game')
        print("------------------------------------------------------------------------------------------") 
        self.game.initialize_tile_bag()
        self.game.put_tiles_in_rack()
        
        while not self.game.game_over():
            self.game.next_turn()
            self.show_board()
            player_number = self.game.get_player_id()
            player_name = self.game.current_player.name  # Accede al nombre del jugador actual
            print("------------------------------------------------------------------------------------------") 
            print(f"Es el Turno del jugador {player_number}: {player_name.title()}")
            print("------------------------------------------------------------------------------------------") 
            self.take_turn()
            self.get_tiles_to_full_rack()
        print("------------------------------------------------------------------------------------------")
        print('¡La partida ha finalizado!')
        print('¡Gracias por Jugar Scrabble Game, vuelva pronto!')
        print("------------------------------------------------------------------------------------------")
        self.show_scores()


if __name__ == "__main__":
    main = Main()
    main.play_scrabble_game()
    
