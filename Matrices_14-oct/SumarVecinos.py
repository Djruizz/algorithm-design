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
            current[c] += a[c+1] if a[c+1] else 0
            current[c] += a[c-1] if a[c-1] else 0
            current[c] += a[f+1] if a[f+1] else 0
            current[c] += a[f-1] if a[f-1] else 0

print(sumarVecinos(A))