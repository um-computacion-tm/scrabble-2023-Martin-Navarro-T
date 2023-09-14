from game.scrabble import ScrabbleGame

def main():
    print("Bienvenido a Scrabble Game")
    try:
        players_count = int(input("Ingrese la cantidad de jugadores: "))

        if players_count <= 1 or players_count > 4:
            print("El número de jugadores debe estar entre 2 y 4.")
        else:
            # Realizar el juego para la cantidad de jugadores especificada
            play_game(players_count)
    except ValueError:
        print("Por favor, ingrese un número válido de jugadores.")
        return  # Terminar el programa si ocurre un error

def play_game(players_count):
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

