import math
x1 = float(input("Ingrese la coordenada X del primer punto (x1): "))
x2 = float(input("Ingrese la coordenada X del segundo punto (x2): "))

y1 = float(input("Ingrese la coordenada Y del primer punto (y1): "))
y2 = float(input("Ingrese la coordenada Y del segundo punto (y2): "))


d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
if(d<0):
    print("Error")
else:
    print("La distancia euclidiana es: ", d)
