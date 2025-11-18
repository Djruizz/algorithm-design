E = int(input())
estrofas = 0

for _ in range(E):
    consonante = input().lower()
    ocurrencias = []

    for _ in range(4):
        verso = input()
        ocurrencias.append(verso.lower().count(consonante))

    if len(set(ocurrencias)) == 1:
        estrofas += 1

print(estrofas)
