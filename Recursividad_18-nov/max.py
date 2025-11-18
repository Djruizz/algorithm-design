lista=[17,21,56,22,9,48,99,13]
def max_recursivo(l):
    if not l:
        return 0
    else:
        if l[0] > max_recursivo(l[1:]):
            return l[0]
    return max_recursivo(l[1:])

print(max_recursivo(lista))