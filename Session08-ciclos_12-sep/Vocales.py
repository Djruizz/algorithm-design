nombre = input("Ingresa tu nombre completo: ").lower()
# vocales = ["a","e","i","o","u"]
count = 0
for i in nombre:
    # if i in vocales:
    #     count +=1
    if i == "a" or i=="e"or i=="i"or i=="o" or i=="u":
        count += 1
print("Vocales ", count)
