M1 = [
    [1,2,3],
    [4,5,6,1],
    [7,8,-1]
]

def valorMac(M):
    maxM = -1
    for f in M:
        for i in f:
            if i > maxM:
                maxM = i
    return maxM

def valorFila(M, fila):
    if fila >= len(M):
        return None
    maxF = -1
    for i in M[fila]:
        if i > maxF:
            maxF = i
    return maxF

def valorCol(M, col):
    if col >= len(M[0]):
        return None
    maxC = -1
    for i in range(len(M)):
        if M[i][col] > maxC:
            maxC = M[i][col]
    return maxC


#---------------------------------------
lEjemplo = [2,9,5,6,3,1]

def threeSum(L, target):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            for k in range(j+1,len(L)):
                if L[i] + L[j] + L[k] == target:
                    return [i,j,k]
    return -1

# print(threeSum(lEjemplo, 18))

def uniqueNums(L):
    r = []
    for i in L:
        if not L.count(i) > 1:
            r.append(i)
    return r

def repeatedNums(L):
    r = []
    for i in L:
        if L.count(i) > 1:
            r.append(i)
    return r

lEjemplo2 = [1,2,2,3,4,4,5,5,6,6,6]
print(uniqueNums(lEjemplo2))
