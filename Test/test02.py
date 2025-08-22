import random

options = ['piedra', 'papel', 'tijera']

def jugar():
    usuario = input("Elige piedra, papel o tijera: ").lower()
    if usuario not in options:
        print("Opción no válida.")
        return
    computadora = random.choice(options)
    print(f"Computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

if __name__ == "__main__":
    jugar()