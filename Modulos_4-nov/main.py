import menu
import data_utils
import student_utils
def main():
    while True:
        menu.showMenu()
        selection = menu.selectOption()
        if selection == 1:
            data_utils.registerStudent()
        elif selection == 2:
            deleteName = input("A quien quieres eliminar? ")
            data_utils.deleteStudent(deleteName, data_utils.students)
        elif selection == 3:
            student_utils.classAverage(data_utils.students)
        elif selection == 4:
            student_utils.showClass(data_utils.students)
        elif selection == 5:
            print("Saliendo del programa")
            break
        
if __name__ == "__main__":
    main()
        