
contador = 0
for i in range(1, 11):
    num1 = i
    for j in range(1, 11):
        num2 = j
        for k in range(1, 11):
            num3 = k
            if (num1 + num2 + num3) == 14:
                print(f"{num1},{num2},{num3}")
                contador += 1
print(contador)