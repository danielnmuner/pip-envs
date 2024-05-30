import random

def get_player_choice():
    """Obtiene la elección del jugador y valida la entrada."""
    while True:
        choice = input("Elige piedra, papel o tijera: ").lower()
        if choice in ["piedra", "papel", "tijera"]:
            return choice
        else:
            print("Elección inválida. Intenta de nuevo.")

def get_computer_choice():
    """Genera una elección aleatoria para la computadora."""
    return random.choice(["piedra", "papel", "tijera"])

def determine_winner(player_choice, computer_choice):
    """Determina el ganador de la ronda."""
    print(f"\nTú elegiste: {player_choice}")
    print(f"La computadora eligió: {computer_choice}")

    if player_choice == computer_choice:
        print("¡Empate!")
    elif (player_choice == "piedra" and computer_choice == "tijera") or \
         (player_choice == "papel" and computer_choice == "piedra") or \
         (player_choice == "tijera" and computer_choice == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

def main():
    """Función principal del juego."""
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        determine_winner(player_choice, computer_choice)

        play_again = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != "s":
            break

if __name__ == "__main__":
    main()