def ocultar(cont):
    oculta = ""
    i = 0
    for c in cont:
        if i == 1 or i == 2:
            oculta += "*"
        else:
            oculta += c
        i += 1
    return oculta

print(ocultar("contraseñaSuperSegura"))