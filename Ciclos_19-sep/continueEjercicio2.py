year = int(input("Ingresa el año: "))
for i in range(year):
    if (i % 4 == 0 and i % 400 == 0) or i % 4 == 0 and i % 100 != 0 :
        print(i)
    else:
        continue
    
        