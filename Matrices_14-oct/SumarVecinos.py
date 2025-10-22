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
            val = 0
            if f > 0 :
                val += a[f-1][c]
            if f < len(a)-1:
                val += a[f+1][c]
            if c > 0:
                val += a[f][c-1]
            if c < len(a[0])-1:
                val += a[f][c+1]
            current.append(val)
        result.append(current)
    return result


print(sumarVecinos(A))