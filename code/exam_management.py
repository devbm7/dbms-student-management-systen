import Database
import Menu
import Student
import Subject
import Exam

Database.DatabaseCreate()
Database.TablesCreate()

while True:
    print("\t\t\t EXAM MANAGEMENT SYSTEM\n")
    print("=====================================================================")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Exam Management")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        Menu.student_manage()
    elif choice == 2:
        Menu.subject_manage()
    elif choice == 3:
        Menu.exam_manage()
    elif choice == 4:
    	break
    else:
        print("Invalid choice !!!")
        x = input("Press any key to continue")
