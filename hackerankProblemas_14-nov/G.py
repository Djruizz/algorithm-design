from math import ceil
d = 0
for i in range(3):
    X,Y = [int(_) for _ in input().split()]
    d += (X**2 + Y**2)**0.5

print(ceil(d))
