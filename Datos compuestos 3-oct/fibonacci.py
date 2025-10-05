def fibo(num):
    lista = [0,1]
    newVal = 0
    for i in range(num):
        newVal = lista[-2] + lista[-1]
        lista.append(newVal)
    return lista

print(fibo(10))

