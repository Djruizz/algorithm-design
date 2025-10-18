A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def sumarVecinos(a):
    result = []
    for f in range(len(a)):
        current = []
        for c in range(len(a[0])):
            current.append(a[c])
            
        result.append(current)
    return result


print(sumarVecinos(A))