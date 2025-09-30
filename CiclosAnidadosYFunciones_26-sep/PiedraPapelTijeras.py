import random

print("¡Bienvenido a Piedra, Papel o Tijera!")
opciones = ["piedra", "papel", "tijera"]

def Juego():
    jugador = input("Escribe piedra, papel o tijera: ").lower().strip()
    if jugador not in opciones:
        print("Opción inválida. Intenta de nuevo.")

    computadora = random.choice(opciones)
    print(f"\nLa computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    print()

Juego()