from game.scrabble import ScrabbleGame

def main():
    print("Bienvenido a Scrabble Game")
    try:
        players_count = int(input("Ingrese la cantidad de jugadores: "))
        if players_count <= 1 or players_count > 4:
            raise ValueError     
    except ValueError:
        print("Valor inválido. Debe ingresar un número entre 2 y 4.")
        return  
    
    scrabble_game = ScrabbleGame(players_count)  

    print(f"Cantidad de Jugadores: {len(scrabble_game.players)}")
    
    while scrabble_game.playing():
        print(f"Turno del Jugador {scrabble_game.current_player.name}") 
        word = input("Ingrese Palabra: ")
        location_x = int(input("Ingrese posición 'X': "))  
        location_y = int(input("Ingrese posición 'Y': "))  
        location = (location_x, location_y)
        orientation = input("Ingrese la orientación (V/H): ").upper() 
        
        if scrabble_game.validate_word(word, location, orientation):
            print("Palabra válida. ¡Bien hecho!")
        else:
            print("Palabra inválida. Inténtelo de nuevo.")

        scrabble_game.next_turn()

if __name__ == '__main__':
    main()


