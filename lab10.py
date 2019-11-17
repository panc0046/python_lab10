import sqlite3
import base64
import webbrowser
import click

# Establish connection with database
conn = sqlite3.connect('D:/code/python/lab-10/week10.db')
cursor = conn.cursor()
print("Opened database successfully")

# Retrieve data from table
cursorData = cursor.execute("select * from Lab10")
studentData = cursorData.fetchall()

def updateRecord(id,country,city):
    cursor.execute("UPDATE Lab10 SET Country = ?, City = ? WHERE id = ?",(country,city,id))
    conn.commit()

# Take user input
quitProgram = True
while(quitProgram == True):
    recordNumber = input("Enter a record number from 1 to "+ str(len(studentData)) +" => ")

    # If user input between expected number
    if(recordNumber != 'q'):
        if int(recordNumber) >= 1 and int(recordNumber) <= len(studentData):
            for i in range(1,len(studentData)+1):
                if i == int(recordNumber):
                    # decode the link
                    decoded = base64.b64decode(studentData[i-1][1]).decode("utf-8")
                    webbrowser.open_new_tab(decoded)
                    country = input("Enter country name that you show in browser => ")
                    city = input("Enter city name that you show in browser => ")
                    updateRecord(recordNumber,country,city)
                    print("Record updated successfully")
                    break
        else:
            print("Enter valid choice")
    else:
        quitProgram = False
        print("Quit the program")
        exit()
