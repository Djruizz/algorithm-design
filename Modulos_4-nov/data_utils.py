students = []
def registerStudent():
    name = input("Nombre del estudiante: ")
    grades = [float(c) for c in input("Ingresa las calificaciones separadas por 1 espacio: ").split()]
    student = {"student_name": name, "student_grades": grades }
    students.append(student)


def deleteStudent(name, students):
    for i in students:
        if i["student_name"].lower() == name.lower():
            print("Estudiante eliminado!")
            students.remove(i)
            break


# def average():
#     avr = 0
#     for student in students:
#         avr += student["student.grades"]
#     return avr / len(students)

