def digitos(num):
    i = 1
    while num >= 10**i:
        i +=1
    return i

print(digitos(32110))
