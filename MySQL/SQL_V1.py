import mysql.connector

# Initialize Database Connection

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "testdb")
print(mydb) 

# Initialize Cursor for Database

mycursor = mydb.cursor()


'''
#? 1. Create Database
    #! mycursor.execute("CREATE DATABASE testdb")

#? 2. Show Database
    #! for db in mycursor:
         print(db)

#? 3. Create Table
    #! mycursor.execute("CREATE TABLE students ( name VARCHAR(255), age INTEGER(10) ) ")

#? 4. Show Table
    #! for tb in mycursor:
          print(tb)

#? 5. Insert Data into Table
    #! sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

        student1 = ("Aaron", 18)
        mycursor.execute(sqlFormula, student1)
        mydb.commit()

#? 6. Insert Multiple Data into Table
    #! sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

        students = [("Aaron", 18), ("John", 18),]
        mycursor.execute(sqlFormula,students)
        mydb.commit()

#? 7. Retrieve Data from Table
    #! mycursor.execute("SELECT * FROM students")

        myresult = mycursor.fetchall()

        for row in my result:
            print(row)


'''