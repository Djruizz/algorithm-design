def primos(i, f):
    for n in range(i,f):
        for j in range(n):
            if n % j == 0:
                print(f"{n} no es primo")
            else:
                print(f"{n} es primo")

primos(1,100)