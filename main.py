import sqlite3
import tkinter
import tkinter.ttk
import tkinter as tk
import tkinter.messagebox

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


def main():  # Creates database and containes first steps of the GUI interface
    curs.execute('''CREATE TABLE IF NOT EXISTS StudentDatabase(student_id INTEGER PRIMARY KEY NOT NULL, 
                first_name TEXT NOT NULL,last_name TEXT NOT NULL, age INTEGER NOT NULL, 
                state TEXT NOT NULL, hobby_one TEXT NOT NULL, hobby_two TEXT NOT NULL)''')

    # This is the actual database, you guys can just change the ###### to whatever you want
    people_info = [(1, 'Mason', 'Baloun', 18, 'MN', 'Art', 'Running'),
                   (2, 'William', 'Brando', 16, 'MN', 'Gaming', 'Building Models'),
                   (3, 'Christian', 'Berry', 18, 'MN', 'Reading', 'Writing'),
                   (4, 'Joe', 'Mama', 18, 'MN', 'Art', 'Running'),
                   (5, 'Yuuji', 'Itadori', 19, 'NY', 'Watching Anime', 'Hanging Out With Friends'),
                   (6, 'Jay', 'Dipersia', 21, 'IL', 'Playing Murder Mystery', 'Art'),
                   (7, 'Ikora', 'Rey', 20, 'PA', 'Reading', 'Stargazing'),
                   (8, 'Isaac', 'Nelson', 16, 'MD', 'Music', 'Exercise'),
                   (9, 'Alex', 'Balken', 18, 'WY', 'Welding', 'Wood Carving'),
                   (10, 'David', 'Conway', 22, 'AZ', 'Reading', 'Gaming'), ]
    curs.executemany('INSERT OR REPLACE INTO StudentDatabase VALUES (?, ?, ?, ?, ?, ?, ?)', people_info)

    Info = tkinter.Label(TopFrame,
                         text="Student Database. Please select Input to input more data, \n Read to read existing data, or Close to save and exit the program.")
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


def Request():  # Show all data inside SQL table
    tkinter = tk.Tk()
    tkinter.geometry("660x250")
    r_set = conn.execute('''SELECT * from StudentDatabase''');
    e = tk.Entry(tkinter, width=15, fg='black')

    student_fields = ('Student ID', "First Name", "Last Name", 'Age', "State", "Hobby One", "Hobby Two")
    s = 0
    for i in range(7):
        e = tk.Entry(tkinter, width=15, fg='black')
        e.grid(row=0, column=i)
        e.insert(tk.END, student_fields[s])

        s += 1

    r = 1
    for student in r_set:
        for c in range(len(student)):
            e = tk.Entry(tkinter, width=15, fg='black')
            e.grid(row=r + 1, column=c)
            e.insert(tk.END, student[c])

        r = r + 1


def Insert():  # Hub for changing student information
    global InsertClicked
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
        curs.execute('''Select * FROM StudentDatabase''')

        IDText = tkinter.Label(BottomFrame, text="Please enter the appropriate Student ID")
        StudentInput = tkinter.Entry(BottomFrame)

        def Give():
            InfoChange()

        EnterButton = tkinter.Button(BottomFrame, text="Enter", command=Give)
        OutLabel.pack()
        IDText.pack()
        StudentInput.pack()
        EnterButton.pack()

        def InfoChange():
            window = tkinter.Tk()
            window.title("Data Entry Form")
            StudentID = StudentInput.get()
            frame = tkinter.Frame(window)
            frame.pack()

            # Saving User Info
            info_frame = tkinter.LabelFrame(frame, text="Add Student Information")
            info_frame.grid(row=0, column=0, padx=15, pady=20)


            first_name_label = tkinter.Label(info_frame, text="First Name")
            first_name_label.grid(row=0, column=0)

            last_name_label = tkinter.Label(info_frame, text="Last Name")
            last_name_label.grid(row=0, column=1)

            hobby_one_label = tkinter.Label(info_frame, text="Hobby One")
            hobby_one_label.grid(row=4, column=0)

            hobby_one_label = tkinter.Label(info_frame, text="Hobby Two")
            hobby_one_label.grid(row=4, column=1)


            # Entry's
            first_name_entry = tkinter.Entry(info_frame)
            first_name_entry.grid(row=1, column=0)

            last_name_entry = tkinter.Entry(info_frame)
            last_name_entry.grid(row=1, column=1)

            hobby_one_entry = tkinter.Entry(info_frame)
            hobby_one_entry.grid(row=5, column=0)

            hobby_two_entry = tkinter.Entry(info_frame)
            hobby_two_entry.grid(row=5, column=1)


            # Age Number Box
            age_label = tkinter.Label(info_frame, text="Age")
            age_spinbox = tkinter.Spinbox(info_frame, from_=18, to=110)
            age_label.grid(row=2, column=0)
            age_spinbox.grid(row=3, column=0)




            # State Information labels
            state_label = tkinter.Label(info_frame, text="State")
            state_combobox = tkinter.ttk.Combobox(info_frame,
                                                  values=['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
                                                          'GA',
                                                          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD',
                                                          'ME',
                                                          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ',
                                                          'NM',
                                                          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
                                                          'TX',
                                                          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'])

            state_label.grid(row=2, column=1)
            state_combobox.grid(row=3, column=1)

            def enter_updated_info():
                firstname = first_name_entry.get()
                lastname = last_name_entry.get()
                state = state_combobox.get()
                age = age_spinbox.get()
                hobbyOne = hobby_one_entry.get()
                hobbyTwo = hobby_two_entry.get()

                conn = sqlite3.connect('StudentDatabase.db')

                curs.execute('UPDATE StudentDatabase SET first_name = ?, last_name=?, age=?, state=?, hobby_one=?, '
                             'hobby_two=? '
                             'WHERE student_id=?',
                             (firstname, lastname, age, state, hobbyOne, hobbyTwo, StudentID))

                conn.commit()

            # Buttons
            UpdateStudentClicked = True
            button = tkinter.Button(frame, text="Enter data", command=enter_updated_info)
            button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
            window.mainloop()

        Change()

def Change():
    global UpdateStudentClicked
    UpdateStudentClicked = False


def NewStudent():
    global UpdateStudentClicked
    global InsertClicked
    if UpdateStudentClicked == False:
        InsertClicked = False
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

            student_info = (11, firstname, 'Baloun', age, state, 'Art', 'Running')
            curs.execute('INSERT INTO StudentDatabase VALUES (?, ?, ?, ?, ?, ?, ?)', student_info)

            conn.commit()

        # Buttons
        UpdateStudentClicked = True
        button = tkinter.Button(frame, text="Enter data", command=enter_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
        window.mainloop()

        Change()


def DeleteStudent():
    window = tk.Tk()
    window.geometry("660x250")
    r_set = conn.execute('''SELECT * from StudentDatabase''')
    e = tk.Entry(window, width=15, fg='black')

    student_fields = ('Student ID', "First Name", "Last Name", 'Age', "State", "Hobby One", "Hobby Two")
    s = 0
    for i in range(7):
        e = tk.Entry(window, width=15, fg='black')
        e.grid(row=0, column=i)
        e.insert(tk.END, student_fields[s])

        s += 1

    r = 1
    for student in r_set:
        for c in range(len(student)):
            e = tk.Entry(window, width=15, fg='black')
            e.grid(row=r + 1, column=c)
            e.insert(tk.END, student[c])

        r = r + 1

    def Grab():
        StudentId = StudentIdEnter.get()
        EnterButton.destroy()
        StudentIdText.destroy()

        StudentIdEnter.destroy()
        info.set(f"Are you sure you would like to permenantly delete the information about {StudentId}?")
        OutLabel.pack()

        def FinalDeleteStudent():
            curs.execute('''DELETE FROM StudentDatabase WHERE student_id == ?''', StudentId)
            tkinter.messagebox.showinfo('Response', f'Deleted StudentID:{StudentId} ')

        YesButton = tkinter.Button(BottomFrame, text="Yes", command=FinalDeleteStudent)

        NoButton = tkinter.Button(BottomFrame, text="No", command=Reset)
        YesButton.pack(side="left")
        NoButton.pack(side="right")

    StudentIdText = tkinter.Label(BottomFrame, text="Student ID:")
    StudentIdEnter = tkinter.Entry(BottomFrame)
    EnterButton = tkinter.Button(BottomFrame, text="Enter", command=Grab)
    StudentIdText.pack(side="left")
    StudentIdEnter.pack(side="left")
    EnterButton.pack()


def Reset():
    mainwindow.destroy()
    main()


if __name__ == '__main__':
    main()
