lista = [1,3,4,2,1,9,8,2,1,1,6]
def contar(l, target):
    if not l:
        return 0
    else:
        if l[0] == target:
            return 1 + contar(l[1:],target)
    return contar(l[1:],target)
    
print(contar(lista,1))