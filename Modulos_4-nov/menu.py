
def showMenu():
    print("Bienvenido al menú!")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Mostrar promedio de la clase")
    print("4. Mostrar estudiantes de la clase")
    print("5. Salir")


def selectOption():
    selection = int(input("Que opción eligirás: "))
    while selection < 1 or selection > 5:
        print("Opción invalida, elije del 1-5")
        selection = int(input("Que opción eligirás: "))
    return selection

