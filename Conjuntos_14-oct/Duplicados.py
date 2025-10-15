l = [1,2,2,3,3,3,4,4,4,4]
def dups(L):
    return len(L) - len(set(L))
    

print(dups(l))

