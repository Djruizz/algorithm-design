import math

angulo = float(input("Ingrese el ángulo en grados: "))
diametro = float(input("Ingrese el diametro de la circunferencia: "))
radio = diametro / 2

angulo_rad = math.radians(angulo)

x = radio * math.cos(angulo_rad)
y = radio * math.sin(angulo_rad)

print(f"El punto en la circunferencia es: ({round(x, 3)}, {round(y, 3)})")