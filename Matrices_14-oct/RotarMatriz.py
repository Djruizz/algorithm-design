def rotar(a):
    nuevaLista = []
    for j in range(len(a[0])):
        current=[]
        for i in range(len(a)):
            current.append(a[i][j])
        nuevaLista.append(current)
    return nuevaLista



A = [
    [1,2,3],
    [4,5,6]
]
for m in rotar(A):
    print(m)
