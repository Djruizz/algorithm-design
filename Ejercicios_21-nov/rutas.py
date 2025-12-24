from functools import cache
@cache
def camino(m,n):
    if m == 0 or n == 0:
        return 1
    return camino(m-1,n) + camino(m,n-1)

    
print(camino(3,3))
