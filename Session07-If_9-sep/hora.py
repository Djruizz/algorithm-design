hora = int(input("ingresa la hora (0-23): "))
mensaje = ""
if hora < 11:
    mensaje+="mañana"
    if hora < 6:
        mensaje = "temprano por la " * mensaje
else:
    mensaje+="tarde"
    if hora < 18:
        mensaje = "temprano por la " * mensaje
print(mensaje)