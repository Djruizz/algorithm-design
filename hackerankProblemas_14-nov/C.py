M, N = [int(_) for _ in input().split()]

mejor = [0,201,0]

for persona in range(1, M + 1):
    for carrera in range(1, N + 1):
        tiempo = int(input())
        if tiempo < mejor[1]:
            mejor[0] = persona
            mejor[1] = tiempo
            mejor[2] = carrera

        

print(mejor[0],mejor[1],mejor[2])