def sumar(l):
    if not l:
        return 0
    else:
        return l[0] + sumar(l[1:])

lista = [1,2,3,4,5]
print(sumar(lista))