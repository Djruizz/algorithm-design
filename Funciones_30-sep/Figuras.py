def circulo():
    radio = int(input("Radio del circulo: "))
    print(f"Area del circulo: {(radio**2) * 3.141592}")

def cuadrado():
    lado = int(input("Lado del cuadrado: "))
    print(f"Area del cuadrado: {lado**2}")

def rectangulo():
    lado1 = int(input("Lado 1 del rectangulo: "))
    lado2 = int(input("Lado 2 del rectangulo: "))
    print(f"Area del rectangulo: {lado1 * lado2}")

def triangulo():
    base = int(input("Base del triangulo: "))
    altura= int(input("Altura del triangulo: "))
    print(f"Area del triagulo: {(base*altura)/2}")

def rombo():
    D = int(input("diagonal mayor del rombo: "))
    d = int(input("diagonal menos del rombo: "))
    print(f"Area del rombo: {(D+d)/2}")

def poligono():
    nLados = int(input("Numero de lados: "))
    lado = int(input("Longitud del lado: "))
    a = int(input("Apotema: "))
    area = ((nLados*lado)*a)/2
    print(f"Area del rombo: {area}")


print("MENÚ:")
print("1. Circulo\n2. Cuadrado\n3. Rectangulo\n4. Triangulo\n5. Rombo\n6. Poligono regular")

figura = int(input("Selecciona el numero de la figura: "))


if figura == 1:
    circulo()
elif figura == 2:
    cuadrado()
elif figura == 3:
    rectangulo()
elif figura == 4:
    triangulo()
elif figura == 5:
    rombo()
elif figura == 6:
    poligono()
else:
    print("Error, opcion no válida")
    



