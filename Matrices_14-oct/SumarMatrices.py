A = [
    [1, 2],
    [4, 5],
]
B = [
    [2,4],
    [3,5]
]
def summ(a,b):
    result = []
    for i in range(len(a)):
        currentList = []
        for j in range(len(a[0])):
            itemSumm = a[i][j] + b[i][j]
            currentList.append(itemSumm)
        result.append(currentList)
    print(result)

summ(A,B)