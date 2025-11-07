word = "AHM PQOUYYM QJFD MX CGS PQQAPUQURQ QEFA"

def cifrar(palabra, d):
    resultado = ""
    abc = {}
    for i in range(26):
        # abc[chr(ord("a") + i)] = chr(ord("a") + (i + d) % 26)
        abc[chr(ord("A") + i)] = chr(ord("A") + (i + d) % 26)
        abc[" "] = " "
    for c in palabra:
        resultado += abc[c]
    return resultado


for j in range(26):
    print(j)
    print(cifrar(word, j))