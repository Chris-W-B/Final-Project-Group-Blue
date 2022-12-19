import sqlite3
import tkinter
import tkinter.ttk
# By Team Blue

mainwindow = tkinter.Tk()
mainwindow.title = "Student Database"
BottomFrame = tkinter.Frame(mainwindow, height=20, width=30)
TopFrame = tkinter.Frame(mainwindow, height=20, width=30, padx=20, pady=20)
conn = sqlite3.connect('StudentDatabase.db')
curs = conn.cursor()
info = tkinter.StringVar()
InsertClicked = False
UpdateStudentClicked = False
OutLabel = tkinter.Label(BottomFrame, textvariable=info)
LeftOverButtons = False



def main(): #Creates database and containes first steps of the GUI interface
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL, 
                first_name TEXT NOT NULL,last_name TEXT NOT NULL, course_one TEXT NOT NULL, 
                course_two TEXT NOT NULL, hobby_one TEXT NOT NULL, hobby_two TEXT NOT NULL)''')

def Database(): #Creates database and containes first steps of the GUI interface
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL,first_name TEXT NOT NULL,
                last_name TEXT NOT NULL, course_one TEXT NOT NULL, course_two TEXT NOT NULL, hobby_one TEXT NOT NULL,
                hobby_two TEXT NOT NULL)''')
        #This is the actual database, you guys can just change the ###### to whatever you want
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000001", "William", "Brando", "16", 
        "MN", "Gaming", "Building Models")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000002", "Christian", "Berry", "########", 
        "########", "########", "#######")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000003", "Mason", "Baloun", "########", 
        "#########", "########", "##########")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000004", "David", "Conway", "17", 
        "MN", "Art", "Creating Graphic Novels")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000005", "Jacob", "Howler", "16", 
        "AZ", "Books", "Making Things")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000006", "Yuuji", "Itadori", "16", 
        "FL", "Watching Anime", "Hanging out with Friends")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000007", "Jay", "Dipersia", "21", 
        "IL", "Playing Murder Mystery", "Art")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000008", "Ikora", "Rey", "19", 
        "MD", "Books", "Studying the Stars")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000009", "Isaac", "Nelson", "16", 
        "CA", "Gaming", "Singing")''')
    curs.execute('''INSERT INTO TABLE StudentDatabase("00000010", "Alex", "Balken", "22", 
        "WY", "Welding", "Wood Carving")''')
    curs.execute('''SELECT * From StudentDatabase''')
    Info = tkinter.Label(TopFrame, text="Student Database. Please select Input to input more data, \n Read to read existing data, or Close to save and exit the program.")
    InputButton = tkinter.Button(TopFrame, text="Input", command=Insert)
    ReadButton = tkinter.Button(TopFrame, text="Read", command=Request)

    def Close():
        conn.commit()
        conn.close()
        mainwindow.destroy()

    CloseButton = tkinter.Button(TopFrame, text="Close", command=Close)
    Info.grid(row=0, column=2)
    InputButton.grid(row=1, column=1)
    ReadButton.grid(row=1, column=2)
    CloseButton.grid(row=1, column=3)
    TopFrame.pack()
    BottomFrame.pack()
    tkinter.mainloop()
    conn.commit()
    conn.close()


def Request(): #Gives all the data in the database
    global LeftOverButtons
    if LeftOverButtons == True:
        List = str(curs.fetchone())
    while List != "None":
        List += "\n"
        List += str(curs.fetchone())
    OutLabel.pack()
    info.set(List)


def Insert(): #Hub for changing student information
    global InsertClicked, LeftOverButtons
    LeftOverButtons = True
    info.set("Would you like to update existing data, delete an existing student, or create a new student?")
    OutLabel.pack()
    if InsertClicked == False:
        def UpdateSuicide():
            DeleteStudentButton.destroy()
            UpdateDataButton.destroy()
            NewStudentButton.destroy()
            UpdateData()

        UpdateDataButton = tkinter.Button(BottomFrame, text="Update Data", command=UpdateSuicide)
        def NewStudentSuicide():
            DeleteStudentButton.destroy()
            UpdateDataButton.destroy()
            NewStudentButton.destroy()
            NewStudent()

        NewStudentButton = tkinter.Button(BottomFrame, text="Create New Student", command=NewStudentSuicide)
        def DeleteSuicide():
            DeleteStudentButton.destroy()
            UpdateDataButton.destroy()
            NewStudentButton.destroy()
            DeleteStudent()

        DeleteStudentButton = tkinter.Button(BottomFrame, text="Delete Student", command=DeleteSuicide)
        UpdateDataButton.pack(side="right")
        DeleteStudentButton.pack(side="left")
        NewStudentButton.pack()
        InsertClicked = True



def UpdateData():
    global UpdateStudentClicked
    if UpdateStudentClicked == False:
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
                                              values=['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                                                      'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
                                                      'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
                                                      'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
                                                      'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'])

        state_label.grid(row=2, column=1)
        state_combobox.grid(row=3, column=1)

        def enter_data():
            firstname = first_name_entry.get()
            lastname = last_name_entry.get()

            state = state_combobox.get()
            age = age_spinbox.get()

            conn = sqlite3.connect('StudentDatabase.db')

            student_info = (1, firstname, lastname)


            curs.execute('INSERT OR REPLACE INTO Something VALUES (?, ?, ?)', student_info)

            conn.commit()

            print(1, firstname, lastname)

        # Buttons
        UpdateStudentClicked = True
        button = tkinter.Button(frame, text="Enter data", command=enter_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
        window.mainloop()

        Change()




def Change():
    global UpdateStudentClicked
    UpdateStudentClicked = False

def NewStudent():
    pass


def DeleteStudent():
    curs.execute('''SELECT student_id, first_name, last_name FROM StudentDatabase''')
    text = str(curs.fetchone())
    info.set(text)
    while text != "None":
        text += "\n"
        text += str(curs.fetchone())

    text += "\nPlease enter the student id of the student you would like to remove from the database"
    def Grab():
        StudentId=StudentIdEnter.get()
        EnterButton.destroy()
        StudentIdText.destroy()

        StudentIdEnter.destroy()
        info.set(f"Are you sure you would like to permenantly delete the information about {StudentId}?")
        OutLabel.pack()
        def FinalDeleteStudent():
            curs.execute('''DELETE FROM StudentDatabase WHERE student_id == ?''', StudentId)

        YesButton = tkinter.Button(BottomFrame, text="Yes", command=FinalDeleteStudent)

        NoButton = tkinter.Button(BottomFrame, text="No")
        YesButton.pack(side="left")
        NoButton.pack(side="right")

    info.set(text)
    StudentIdText = tkinter.Label(BottomFrame, text="Student ID:")
    StudentIdEnter = tkinter.Entry(BottomFrame)
    EnterButton = tkinter.Button(BottomFrame, text="Enter", command=Grab)
    StudentIdText.pack(side="left")
    StudentIdEnter.pack(side="left")
    EnterButton.pack()


if __name__ == '__main__':
    main()
