import sqlite3
import tkinter
import tkinter.ttk
# By Team Blue

mainwindow = tkinter.Tk()
mainwindow.title = "Student Database"
BottomFrame = tkinter.Frame(mainwindow, height=30, width=30)
TopFrame = tkinter.Frame(mainwindow, height=30, width=30)
conn = sqlite3.connect('StudentDatabase.db')
curs = conn.cursor()
info = tkinter.StringVar()
InsertClicked = False
OutLabel = tkinter.Label(BottomFrame, textvariable=info)


def main(): #Creates database and containes first steps of the GUI interface
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL, 
                first_name TEXT NOT NULL,last_name TEXT NOT NULL, course_one TEXT NOT NULL, 
                course_two TEXT NOT NULL, hobby_one TEXT NOT NULL, hobby_two TEXT NOT NULL)''')
    curs.execute('''SELECT * From StudentDatabase''')
    Info = tkinter.Label(TopFrame, text="Student Database. Please select Input to input more data, \nor Read to read existing data")
    InputButton = tkinter.Button(TopFrame, text="Input", command=Insert)
    ReadButton = tkinter.Button(TopFrame, text="Read", command=Request)
    Info.pack()
    InputButton.pack()
    ReadButton.pack()
    TopFrame.pack()
    BottomFrame.pack()
    tkinter.mainloop()
    conn.commit()
    conn.close()

def Request(): #Gives all the data in the database
    List = str(curs.fetchone())
    while List != "None":
        List += "\n"
        List += str(curs.fetchone())
    OutLabel.pack()
    info.set(List)


def Insert(): #Hub for changing student information
    global InsertClicked
    info.set("Would you like to update existing data, delete an existing student, or create a new student?")
    OutLabel.pack()
    if InsertClicked == False:
        UpdateDataButton = tkinter.Button(BottomFrame, text="Update Data", command=UpdateData)
        NewStudentButton = tkinter.Button(BottomFrame, text="Create New Student", command=NewStudent)
        DeleteStudentButton = tkinter.Button(BottomFrame, text="Delete Student", command=DeleteStudent)
        UpdateDataButton.pack(side="right")
        DeleteStudentButton.pack(side="left")
        NewStudentButton.pack()
        InsertClicked = True



def UpdateData():
    window = tkinter.Tk()
    window.title("Data Entry Form")

    frame = tkinter.Frame(window)
    frame.pack()

    # Saving User Info
    info_frame = tkinter.LabelFrame(frame, text="Add Student Information")
    info_frame.grid(row=0, column=0, padx=15, pady=20)

    first_name_label = tkinter.Label(info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)

    last_name_label = tkinter.Label(info_frame, text="Last Name")
    last_name_label.grid(row=0, column=1)

    # Entry's
    first_name_entry = tkinter.Entry(info_frame)
    last_name_entry = tkinter.Entry(info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    # Age Number Box
    age_label = tkinter.Label(info_frame, text="Age")
    age_spinbox = tkinter.Spinbox(info_frame, from_=18, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    # State Information labels
    state_label = tkinter.Label(info_frame, text="State")
    state_combobox = tkinter.ttk.Combobox(info_frame,
                                  values=['MN', 'NY'])

    state_label.grid(row=2, column=1)
    state_combobox.grid(row=3, column=1)

    # Buttons
    button = tkinter.Button(frame, text="Enter data")
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    window.mainloop()

def NewStudent():
    print("test")
    pass


def DeleteStudent():
    curs.execute('''SELECT student_id, first_name, last_name FROM StudentDatabase''')
    text = str(curs.fetchone())
    info.set(text)
    while text != "None":
        text += "\n"
        text += str(curs.fetchone())
    if text == "None":
        info.set("Database is empty!")
        return 1
    text += "\nPlease enter the student id of the student you would like to remove from the database"
    info.set(text)



if __name__ == '__main__':
    main()
