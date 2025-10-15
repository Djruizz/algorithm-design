def primos(i, f):
    for n in range(i,f):
        esPrimo = False
        for j in range(2,n):
            if n % j == 0:
                esPrimo = False
                break
            esPrimo = True
        if esPrimo:
            print(f"{n} es primo")
        else:
            print(f"{n} no es primo")

primos(1,100)