n = int(input("ingrese el numero de filas: "))
for f in range(n):
    print("*"*f)

print("")

for f in range(n):
    print("*"*(n-f))