import Student
import Subject
import Exam

def student_manage():
    while True:
        print("\t\t\t STUDENT RECORD MANAGEMENT\n")
        print("==========================================================")
        print("1. Add Student")
        print("2. Search Student Record")
        print("3. Delete Student Record")
        print("4. Update Record")
        print("5. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Student.insertData()
        elif choice == 2:
            Student.SearchStudentRec()
        elif choice == 3:
            Student.deleteStudent()
        elif choice == 4:
            Student.UpdateStudent()
        elif choice == 5:
            return
        else:
            print("Invalid choice !!!")
            x = input("Enter any key to continue")

def subject_manage():
	while True:
		print("\t\t\t SUBJECT RECORD MANAGEMENT\n")
		print("==========================================================")
		print("1. Add Subject Record")
		print("2. Search Subject Record")
		print("3. Delete Subject Record")
		print("4. Update Subject Record")
		print("5. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter your choice: "))
		if choice == 1:
			Subject.insertSubject()
		elif choice == 2:
			Subject.SearchSubject()
		elif choice == 3:
			Subject.deleteSubject()
		elif choice == 4:
			Subject.UpdateSubject()
		elif choice == 5:
			return
		else:
			print("Invalid choice !!!")
			x = input("Enter any key to continue")

def exam_manage():
	while True:
		print("\t\t\t MEMBER RECORD MANAGEMENT\n")
		print("==========================================================")
		print("1. Add Exam")
		print("2. Delete Exam")
		print("3. View Exam")
		print("4. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter your choice: "))
		if choice == 1:
		    Exam.AddExam()
		elif choice == 2:
		    Exam.DeleteExam()
		elif choice == 3:
		    Exam.ViewExam()
		elif choice == 4:
		    return
		else:
		    print("Invalid choice !!!")
		    x = input("Enter any key to continue")
