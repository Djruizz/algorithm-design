import time
from functools import cache
def fibo_i(n):
    sec = [0,1]
    for i in range(1,n+1):
        sec.append(sec[-1]+sec[-2])
    return sec[n]

@cache
def fibo_r(n):
    if n <= 1:
        return n
    else:
        return fibo_r(n-1) + fibo_r(n-2)

startTime = time.time()
numeroFibo = fibo_i(10)
endTime = time.time()

print(f"Tiempo {(endTime-startTime)*1000}ms")
print(f"Fibonacci: {numeroFibo}")

startTime = time.time()
numeroFibo = fibo_r(10)
endTime = time.time()

print(f"Tiempo {(endTime-startTime)*1000}ms")
print(f"Fibonacci: {numeroFibo}")