palabra = input("Ingresa una palabra: ")
sinVocal = ""
for i in palabra:
    if i in "aeiou":
        continue
    sinVocal += i
print(sinVocal)