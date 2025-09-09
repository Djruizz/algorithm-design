calificacion = float(input("Ingresa la calificacion 0-10: "))
mensaje = ""
if(calificacion < 6 and calificacion >=0):
    mensaje += "Necesitas mejorar"
elif(calificacion < 7):
    mensaje += "Te salvaste"
elif(calificacion < 9):
    mensaje += "Nada mal"
elif (calificacion < 10):
    mensaje += "Muy bien"
elif(calificacion == 10):
    mensaje += "Impresionante"
else:
    mensaje += "calificacion invalida"
print(mensaje)