import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import os


def AddExam():
    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = 'Manav_Patel@2003',database = 'online_exam')
    Cursor = cnx.cursor()
    Exam_ID  = input("Enter Exam_ID : ")
    User_ID = input("Enter User_ID : ")
    Subject_ID = input("Enter Subject_ID : ")
    Exam_Link= input("Enter Exam Link: ")
    Qry = ("INSERT INTO Exam VALUES (%s, %s, %s, %s)")
    data = (Exam_ID, User_ID, Subject_ID, Exam_Link)
    Cursor.execute(Qry,data)
    cnx.commit()
    Cursor.close()
    cnx.close()
    print("Record Inserted.")
    cnx.close()

def DeleteExam():
	cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = 'Manav_Patel@2003',database = 'online_exam')
	Cursor = cnx.cursor()
	Exam_ID = input("Enter Exam_ID of Exam to be deleted: ")
	Qry = ("""DELETE FROM Exam WHERE Exam_ID = %s""")
	del_rec = (Exam_ID,)
	Cursor.execute(Qry, del_rec)
	cnx.commit()
	Cursor.close()
	cnx.close()
	print(Cursor.rowcount, "Record(s) Deleted Successfully.")
	cnx.close()

def ViewExam():
	try:
	    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = 'Manav_Patel@2003',database = 'online_exam')
	    Cursor = cnx.cursor()
	    Exam_ID = input("Enter Exam_ID of Exam to be searched: ")
	    query = ("SELECT * FROM Exam WHERE Exam_ID = %s ")
	    rec_srch = (Exam_ID,)
	    Cursor.execute(query, rec_srch)
	    Rec_count = 0
	    for(Exam_ID, User_ID,Subject_ID, Exam_Link) in Cursor:
	        Rec_count += 1
	        print("=============================================================")
	        print("Exam ID : ", Exam_ID)
	        print("User ID : ", User_ID)
	        print("Subject ID : ", Subject_ID)
	        print("Exam link: ", Exam_Link)
	        print("=============================================================")
	        if Rec_count%2 == 0:
	            input("Press any key to continue")
	            clrscreen()
	            print(Rec_count, "Record(s) found")
	    cnx.commit()
	    Cursor.close()
	    cnx.close()
	except mysql.connector.ERROR as err:
	    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	        print("Something is wrong with your user name or password")
	    elif err.errno == errorcode.ER_BAD_DB_ERROR:
	        print("Database does not exist")
	    else:
	        print(err)
	    cnx.close()
