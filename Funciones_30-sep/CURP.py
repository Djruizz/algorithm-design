
def CURP(nombre, apellidoP, apellidoM, dia, mes, anio, estado, sexo):
    Curp = ""

    Curp += apellidoP[0:2]
    Curp += apellidoM[0]
    Curp += nombre[0]

    Curp += str(anio)[2:]
    if mes < 10:
        Curp += "0"
    Curp += str(mes)

    if dia < 10:
        Curp += "0"
    Curp += str(dia)


    Curp += sexo[0]
    Curp += estado[0:2]
    
    Curp += "XXXXX"
    return Curp.upper()

miCurp = CURP("Dario", "Ruiz", "Padilla", 31, 10, 2007, "Jalisco", "Masculino")
print(miCurp)
