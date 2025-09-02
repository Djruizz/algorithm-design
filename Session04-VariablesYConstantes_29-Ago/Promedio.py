cal1 = float(input("Ingresa la calificacion 1: "))
cal2 = float(input("Ingresa la calificacion 2: "))
tareas = float(input("Ingresa el promedio de las tareas: "))

porcentaje1 = cal1 * 0.2
porcentaje2 = cal2 * 0.2
tareasProm = tareas * 0.6

promedio = (porcentaje1 + porcentaje2 + tareasProm)

print("El promedio final es: ", promedio)