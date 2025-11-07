
def showClass(Sclass):
    print("\n")
    for student in Sclass:
        print(f"Nombre: {student["student_name"]}, Calificaciones: {student["student_grades"]}")

    print("\n")

def studentAverage(student):
    avr = 0 
    for grade in student["student_grades"]:
        avr+=grade
    return avr / len(student["student_grades"])

def classAverage(Sclass):
    classAvr = 0
    for student in Sclass:
        classAvr += studentAverage(student)
    print("El promedio de la clase es: ",classAvr / len(Sclass))
