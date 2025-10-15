def whoRepeats(clase1, clase2):
    return set(clase1).intersection(clase2)

C1 = ["Juan", "Luis", "Ana", "Jose"]
C2 = ["Ana","Martin","Ruben","Maria"]

print(whoRepeats(C1,C2))