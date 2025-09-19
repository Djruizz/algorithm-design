palabra = input("Ingresa una palabra: ").lower()
contador = 0
for i in palabra:
    print("Letra actual: ", i)
    if i == "a":
        contador += 1
    print("contador de a's: ", contador)
    if contador >= 2:
        print("la palabra tiene mas de 1 'a'")
        break