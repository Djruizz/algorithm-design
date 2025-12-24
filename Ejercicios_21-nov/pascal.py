def pascal(n):
    if n < 2:
        return [[1]]
    triangulo = pascal(n-1)
    ultima = triangulo[-1]
    nueva = [1]
    if len(ultima)>= 2:
        for i in range(1,len(ultima)):
            nueva.append(ultima[i]+ultima[i-1])
    nueva.append(1)
    triangulo.append(nueva)
    return triangulo

print(pascal(5))