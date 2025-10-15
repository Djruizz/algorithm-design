a = "a"
b = "e"

def remplazar(a,b,texto):
    limpio = ""
    for c in texto:
        if c == a:
            limpio += b
        else:
            limpio += c
    return limpio

print(remplazar(a,b,"arbol de tamarindo"))