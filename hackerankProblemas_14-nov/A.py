n = input()
f = 1
resultado = 0
for i in n[::-1]:
    resultado += int(i)*f
    f *= -1

if resultado > 0:
    print("Positiva")
elif resultado < 0:
    print("Negativa")
else:
    print("ERROR")