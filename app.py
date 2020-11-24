import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from Supporting_Programs.admin import *
from Supporting_Programs.database import *
from Supporting_Programs.student import *
from Supporting_Programs.staff import *
from Supporting_Programs.databaseSS import *
import os
from fpdf import FPDF 
import matplotlib.pyplot as plt
from datetime import date 
from Supporting_Programs.pdfCreator import *
from Supporting_Programs.idCardCreator import idGenerator

Large_Font = ("Verdana", 15)
Small_Font = ("Verdana", 12)


class MainApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self,"Admin Management System") 
        tk.Tk.geometry(self, "1480x780+0+0")

        title = tk.Label(self, text = "Admin Management System", font = Large_Font, bg = "dark turquoise", fg = "black")
        title.pack(side = "top", fill = "both")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True, padx = 10, pady = 10)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (HomePage, AdminSetting, StudentManagement, ViewAllStudent, EnterMarks, ReportCard, StaffManagement, ViewAllStaff):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Home Page", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        def adminCall():
            password = simpledialog.askstring("Enter Password", "Password", show = "*")
            a = Admin()
            actualPassword = a.password
            if password == actualPassword:
                controller.show_frame(AdminSetting)
            else:
                messagebox.showwarning("Warning!!!", "Enter the Correct Password!!!")

        buttonAdmin = tk.Button(self, text = "Admin Settings", height = 20, width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: adminCall())
        buttonAdmin.pack(side = "left", padx = 135)

        buttonStaff = tk.Button(self, text = "Staff Management", height = 20, width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StaffManagement))
        buttonStaff.pack(side = "left", padx = 135)

        buttonStudent = tk.Button(self, text = "Student Management", height = 20, width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StudentManagement))
        buttonStudent.pack(side = "left", padx = 135)
    
class AdminSetting(tk.Frame):

    def __init__(self, parent, controller):
        self.a = Admin()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Admin Page", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        changeYearFrame = tk.Frame(self,bd= 0, relief = "raised")
        changeYearFrame.place(x = 20, y=100, width = 1400)
        printYear = tk.Label(changeYearFrame, text = "Current Year: " + str(self.a.year), font = Large_Font)
        printYear.grid(row = 0, column= 0, padx = 10)
        changeYearEntry = tk.Entry(changeYearFrame)
        changeYearEntry.grid(row = 0, column= 1, padx = 10)
        changeYear = tk.Button(changeYearFrame, text = "Change Year", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: [self.a.change_year(changeYearEntry.get()), changeYearEntry.delete(0, tk.END), printYear.config(text = "Current Year: " + str(self.a.year))])
        changeYear.grid(row = 0, column= 2, padx = 10)

        changeAdminFrame = tk.Frame(self,bd= 0, relief = "raised")
        changeAdminFrame.place(x = 20, y=200, width = 1400)
        printAdmin = tk.Label(changeAdminFrame, text = "Current Admin: " + str(self.a.name), font = Large_Font)
        printAdmin.grid(row = 0, column= 0, padx = 10)
        changeAdminEntry = tk.Entry(changeAdminFrame)
        changeAdminEntry.grid(row = 0, column= 1, padx = 10)
        changeAdmin = tk.Button(changeAdminFrame, text = "Change Admin", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: [self.a.change_admin(changeAdminEntry.get()),changeAdminEntry.delete(0, tk.END), printAdmin.config(text = "Current Admin: " + str(self.a.name))])
        changeAdmin.grid(row = 0, column= 2, padx = 10)

        changeSemesterFrame = tk.Frame(self,bd= 0, relief = "raised")
        changeSemesterFrame.place(x = 20, y=300, width = 1400)
        printSemester = tk.Label(changeSemesterFrame, text = "Current Semester: " + str(self.a.semester), font = Large_Font)
        printSemester.grid(row = 0, column= 0, padx = 10)
        changeSemester = tk.Button(changeSemesterFrame, text = "Change Semester", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: [self.a.change_semester(), printSemester.config(text = "Current Semester: " + str(self.a.semester))])
        changeSemester.grid(row = 0, column= 2, padx = 10)

        changePasswordFrame = tk.Frame(self,bd= 0, relief = "raised")
        changePasswordFrame.place(x = 20, y=400, width = 1400)
        changePasswordEntry = tk.Entry(changePasswordFrame, font = Large_Font)
        changePasswordEntry.grid(row = 0, column= 1, padx = 10)
        changePassword = tk.Button(changePasswordFrame, text = "Change Password", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: [self.a.change_password(changePasswordEntry.get()),changePasswordEntry.delete(0, tk.END)])
        changePassword.grid(row = 0, column= 2, padx = 10)

        backButton = tk.Button(self, text = "Back To Home", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(HomePage))
        backButton.pack(side = "bottom", pady = 10, padx = 10)

class StudentManagement(tk.Frame):

    outputList = "None"
    def __init__(self, parent, controller):
        self.s = Student()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Student Management Page", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        #####Instructions Frame####
        insFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        insFrame.place(x = 0, y = 50, width = 1480, height = 70)
        ins1 = tk.Label(insFrame, text = "1. To add a student, enter input in all the fields and click Add.", font = Small_Font, bg = "dark turquoise")
        ins1.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
        ins2 = tk.Label(insFrame, text = "2. To modify a student, enter the roll number in the input field in left frame and enter those details which are needed to be changed and click modify.", font = Small_Font, bg = "dark turquoise")
        ins2.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)

        #####Input Frame###########
        inputFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        inputFrame.place(x = 40, y = 150, width = 600, height = 450)
        
        name = tk.Label(inputFrame, text = "Name: ", font = Large_Font, bg = "dark turquoise")
        name.grid(row = 0, column= 0, padx = 10, pady = 5)
        nameEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        nameEntry.grid(row = 0, column= 1, padx = 10, pady = 5)
        
        dept = tk.Label(inputFrame, text = "Department: ", font = Large_Font, bg = "dark turquoise")
        dept.grid(row = 1, column= 0, padx = 10, pady = 5)
        deptEntry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        deptval = ["CSE", "ECE"]
        deptEntry["values"] = (deptval)
        deptEntry.grid(row = 1, column= 1, padx = 10, pady = 5)
        
        roll = tk.Label(inputFrame, text = "Roll No.: ", font = Large_Font, bg = "dark turquoise")
        roll.grid(row = 2, column= 0, padx = 10, pady = 5)
        rollEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        rollEntry.grid(row = 2, column= 1, padx = 10, pady = 5)
        
        year = tk.Label(inputFrame, text = "Year: ", font = Large_Font, bg = "dark turquoise")
        year.grid(row = 3, column= 0, padx = 10, pady = 5)
        yearEntry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        yearval = ["1st", "2nd", "3rd", "4th"]
        yearEntry["values"] = (yearval)
        yearEntry.grid(row = 3, column= 1, padx = 10, pady = 5)
        
        hostel = tk.Label(inputFrame, text = "Hostel: ", font = Large_Font, bg = "dark turquoise")
        hostel.grid(row = 4, column= 0, padx = 10, pady = 5)
        hostelEntry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        hostelEntry["values"] = (
            "Yes",
            "No"
        )
        hostelEntry.grid(row = 4, column= 1, padx = 10, pady = 5)

        course1 = tk.Label(inputFrame, text = "Course 1: ", font = Large_Font, bg = "dark turquoise")
        course1.grid(row = 5, column= 0, padx = 10, pady = 5)
        course1Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course1Entry["values"] = (
            "MATHS 1",
            "MATHS 2",
            "NMPT"
        )
        course1Entry.grid(row = 5, column= 1, padx = 10, pady = 5)

        course2 = tk.Label(inputFrame, text = "Course 2: ", font = Large_Font, bg = "dark turquoise")
        course2.grid(row = 6, column= 0, padx = 10, pady = 5)
        course2Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course2Entry["values"] = (
            "INTRODUCTION TO PROGRAMMING",
            "DATA STRUCTURES",
            "DATA STRUCTURES WITH APPLICATIONS"
        )
        course2Entry.grid(row = 6, column= 1, padx = 10, pady = 5)

        course3 = tk.Label(inputFrame, text = "Course 3: ", font = Large_Font, bg = "dark turquoise")
        course3.grid(row = 7, column= 0, padx = 10, pady = 5)
        course3Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course3Entry["values"] = (
            "ANALOG ELECTRONICS",
            "DIGITAL ELECTRONICS",
            "MICROPROCESSOR AND INTERFACING"
        )
        course3Entry.grid(row = 7, column= 1, padx = 10, pady = 5)

        course4 = tk.Label(inputFrame, text = "Course 4: ", font = Large_Font, bg = "dark turquoise")
        course4.grid(row = 8, column= 0, padx = 10, pady = 5)
        course4Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course4Entry["values"] = (
            "COMPUTER SYSTEM ORGANISAION",
            "APPLICATION PROGRAMMING",
            "ELECTRICAL CIRCUITS"
        )
        course4Entry.grid(row = 8, column= 1, padx = 10, pady = 5)

        course5 = tk.Label(inputFrame, text = "Course 5: ", font = Large_Font, bg = "dark turquoise")
        course5.grid(row = 9, column= 0, padx = 10, pady = 5)
        course5Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course5Entry["values"] = (
            "OBJECT ORIENTED PROGRAMMING",
            "APPLIED SCIENCE",
            "MECHANICS AND GRAPHICS"
        )
        course5Entry.grid(row = 9, column= 1, padx = 10, pady = 5)

        course6 = tk.Label(inputFrame, text = "Course 6: ", font = Large_Font, bg = "dark turquoise")
        course6.grid(row = 10, column= 0, padx = 10, pady = 5)
        course6Entry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        course6Entry["values"] = (
            "ENVIRONMENTAL STUDIES",
            "COMMUNICATIONS SKILLS",
            "IT WORKSHOP1"
        )
        course6Entry.grid(row = 10, column= 1, padx = 10, pady = 5)

        def getInput():
            Sname = nameEntry.get()
            Sroll = rollEntry.get()
            Sdept = deptEntry.get()
            Syear = yearEntry.get()
            Shostel = hostelEntry.get()
            Sc1 = course1Entry.get()
            Sc2 = course2Entry.get()
            Sc3 = course3Entry.get()
            Sc4 = course4Entry.get()
            Sc5 = course5Entry.get()
            Sc6 = course6Entry.get()
            Slist = [Sname, Sroll, Sdept, Syear, Shostel, Sc1, Sc2, Sc3, Sc4, Sc5, Sc6]
            return Slist
        
        def deleteEntryFields():
            nameEntry.delete(0, tk.END)
            rollEntry.delete(0, tk.END)
            deptEntry.delete(0, tk.END)
            yearEntry.delete(0, tk.END)
            hostelEntry.delete(0, tk.END)
            course1Entry.delete(0, tk.END)
            course2Entry.delete(0, tk.END)
            course3Entry.delete(0, tk.END)
            course4Entry.delete(0, tk.END)
            course5Entry.delete(0, tk.END)
            course6Entry.delete(0, tk.END)
        
        def addStudent():
            checkList = search("Databases\\student","roll number",rollEntry.get())
            if checkList[0] == "Not Available":
                entryList = getInput()
                if "" in entryList:
                    messagebox.showwarning("Warning!!!", "No Entry field should remain empty!!!")
                else:
                    self.s.add_student(entryList)
                    deleteEntryFields()
            else:
                messagebox.showwarning("Warning!!!", "The Roll Number already exists")
                
        def modifyStudent():
            checkList = search("Databases\\student","roll number",rollEntry.get())
            if rollEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please Enter the roll number to modify!!")
            elif checkList[0] == "Not Available":
                messagebox.showwarning("Warning!!!", "The Roll Number does not exist!\n Add it first")
            else:
                self.s.modify_student(getInput())
                deleteEntryFields()

        viewButtonFrame1 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewButtonFrame1.place(x = 40, y = 600, width = 600, height = 70)
        addButton = tk.Button(viewButtonFrame1, text = "Add", font = Large_Font, width = 15, bg = "dark turquoise", command = lambda: addStudent())
        addButton.grid(row = 0, column = 1, padx = 47, pady = 10)
        modifyButton = tk.Button(viewButtonFrame1, text = "Modify", font = Large_Font, width = 15, bg = "dark turquoise", command = lambda: modifyStudent())
        modifyButton.grid(row = 0, column = 2, padx = 47, pady = 10)

        #####View Frame###############
        viewFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewFrame.place(x = 740, y = 200, width = 700, height = 400)

        def searchDetails(rollno):
            self.outputList = search("Databases\\student","roll number",rollno)

        nameV1 = tk.Label(viewFrame, text = "Name: ", font = Large_Font, bg = "dark turquoise")
        nameV1.grid(row = 1, column= 0, padx = 10, pady = 3)
        nameV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        nameV2.grid(row = 1, column= 1, padx = 10, pady = 3)
        
        deptV1 = tk.Label(viewFrame, text = "Department: ", font = Large_Font, bg = "dark turquoise")
        deptV1.grid(row = 2, column= 0, padx = 10, pady = 3)
        deptV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        deptV2.grid(row = 2, column= 1, padx = 10, pady = 3)

        rollV1 = tk.Label(viewFrame, text = "Roll No.: ", font = Large_Font, bg = "dark turquoise")
        rollV1.grid(row = 3, column= 0, padx = 10, pady = 3)
        rollV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        rollV2.grid(row = 3, column= 1, padx = 10, pady = 3)

        yearV1 = tk.Label(viewFrame, text = "Year: ", font = Large_Font, bg = "dark turquoise")
        yearV1.grid(row = 4, column= 0, padx = 10, pady = 3)
        yearV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        yearV2.grid(row = 4, column= 1, padx = 10, pady = 3)

        hostelV1 = tk.Label(viewFrame, text = "Hostel: ", font = Large_Font, bg = "dark turquoise")
        hostelV1.grid(row = 5, column= 0, padx = 10, pady = 3)
        hostelV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        hostelV2.grid(row = 5, column= 1, padx = 10, pady = 3)

        course1V1 = tk.Label(viewFrame, text = "Course 1: ", font = Large_Font, bg = "dark turquoise")
        course1V1.grid(row = 6, column= 0, padx = 10, pady = 3)
        course1V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course1V2.grid(row = 6, column= 1, padx = 10, pady = 3)

        course2V1 = tk.Label(viewFrame, text = "Course 2: ", font = Large_Font, bg = "dark turquoise")
        course2V1.grid(row = 7, column= 0, padx = 10, pady = 3)
        course2V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course2V2.grid(row = 7, column= 1, padx = 10, pady = 3)

        course3V1 = tk.Label(viewFrame, text = "Course 3: ", font = Large_Font, bg = "dark turquoise")
        course3V1.grid(row = 8, column= 0, padx = 10, pady = 3)
        course3V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course3V2.grid(row = 8, column= 1, padx = 10, pady = 3)

        course4V1 = tk.Label(viewFrame, text = "Course 4: ", font = Large_Font, bg = "dark turquoise")
        course4V1.grid(row = 9, column= 0, padx = 10, pady = 3)
        course4V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course4V2.grid(row = 9, column= 1, padx = 10, pady = 3)

        course5V1 = tk.Label(viewFrame, text = "Course 5: ", font = Large_Font, bg = "dark turquoise")
        course5V1.grid(row = 10, column= 0, padx = 10, pady = 3)
        course5V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course5V2.grid(row = 10, column= 1, padx = 10, pady = 3)

        course6V1 = tk.Label(viewFrame, text = "Course 6: ", font = Large_Font, bg = "dark turquoise")
        course6V1.grid(row = 11, column= 0, padx = 10, pady = 3)
        course6V2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        course6V2.grid(row = 11, column= 1, padx = 10, pady = 3)

        def updateLabels(rollno):
            nameV2.config(text =  str(self.outputList[0]))
            deptV2.config(text = str(self.outputList[1]))
            rollV2.config(text = str(rollno))
            yearV2.config(text = str(self.outputList[2]))
            hostelV2.config(text = str(self.outputList[3]))
            course1V2.config(text = str(self.outputList[4]))
            course2V2.config(text = str(self.outputList[5]))
            course3V2.config(text = str(self.outputList[6]))
            course4V2.config(text = str(self.outputList[7]))
            course5V2.config(text = str(self.outputList[8]))
            course6V2.config(text = str(self.outputList[9]))


        searchFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        searchFrame.place(x = 740, y = 150, width = 700, height = 50)
        printquery = tk.Label(searchFrame, text = "Enter a Roll Number to search: " , font = Small_Font, bg = "dark turquoise")
        printquery.grid(row = 0, column= 0, padx = 5, pady = 10)
        rollNoEntry = tk.Entry(searchFrame)
        rollNoEntry.grid(row = 0, column= 1, padx = 5, pady = 10)

        def searchButtonCall():
            if rollNoEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please enter the roll number before pressing search!!!")
            else:
                searchDetails(rollNoEntry.get())
                updateLabels(rollNoEntry.get())

        searchButton = tk.Button(searchFrame, text = " Search ", width = 12, bg = "dark turquoise", font = Small_Font, command = lambda: searchButtonCall())
        searchButton.grid(row = 0, column= 2, padx = 5, pady = 10)
        addMarksButton = tk.Button(searchFrame, text = " Add Marks ", width = 12, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(EnterMarks))
        addMarksButton.grid(row = 0, column= 3, padx = 5, pady = 10)

        def deleteButtonCall():
            if rollNoEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please enter the roll number and search before deleting!!!")
            else:
                deleteRecord("Databases\\student", rollNoEntry.get())
                deleteRecord("Databases\\studentMarks", rollNoEntry.get())
                searchDetails(rollNoEntry.get())
                updateLabels(rollNoEntry.get())
                rollNoEntry.delete(0, tk.END)

        viewButtonFrame2 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewButtonFrame2.place(x = 740, y = 600, width = 700, height = 70)
        deleteButton = tk.Button(viewButtonFrame2, text = "Delete", font = Large_Font, bg = "dark turquoise", width = 15, command = lambda: deleteButtonCall())
        deleteButton.grid(row = 0, column = 1, padx = 12, pady = 10)
        viewAllButton = tk.Button(viewButtonFrame2, text = "View All", font = Large_Font, bg = "dark turquoise", width = 15, command = lambda: controller.show_frame(ViewAllStudent))
        viewAllButton.grid(row = 0, column = 2, padx = 12, pady = 10)
        viewGCardButton = tk.Button(viewButtonFrame2, text = "View Grade Card", font = Large_Font, bg = "dark turquoise", width = 15, command = lambda: controller.show_frame(ReportCard))
        viewGCardButton.grid(row = 0, column = 3, padx = 12, pady = 10)
        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Home", width = 20, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(HomePage))
        backButton.pack(side = "bottom", pady = 10, padx = 10)

class ViewAllStudent(tk.Frame):

    def __init__(self, parent, controller):
        self.s = Student()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "View All Details", font = Large_Font)
        label.pack(pady = 10, padx = 10)
        viewAllFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewAllFrame.place(x = 250, y = 100, width = 1000, height = 580)
        scrollbar1 = tk.Scrollbar(viewAllFrame)
        scrollbar2 = tk.Scrollbar(viewAllFrame, orient = "horizontal")
        scrollbar1.pack(side = "right", fill = 'y')
        scrollbar2.pack(side = "bottom", fill = 'x')
        totalEntries, details = get_details("Databases\\student")
        detailsList = tk.Listbox(viewAllFrame, yscrollcommand = scrollbar1.set, xscrollcommand = scrollbar2.set, bg = "dark turquoise", width = 900, font = Small_Font)
        def refreshPage():
            detailsList.delete(0, tk.END)
            totalEntries, details = get_details("Databases\\student")
            for i in range(1, totalEntries+1):
                detailsList.insert(tk.END, f"{i}. Name: {details[i][0]}     Dept: {details[i][1]}     Roll no.: {details[i][2]}     Year: {details[i][3]}     Hostel: {details[i][4]}     Course 1: {details[i][5]}     Course 2: {details[i][6]}     Course 3: {details[i][7]}     Course 4: {details[i][8]}     Course 5: {details[i][9]}     Course 6: {details[i][10]}")
                detailsList.insert(tk.END, " ")

        for i in range(1, totalEntries+1):
            detailsList.insert(tk.END, f"{i}. Name: {details[i][0]}     Dept: {details[i][1]}     Roll no.: {details[i][2]}     Year: {details[i][3]}     Hostel: {details[i][4]}     Course 1: {details[i][5]}     Course 2: {details[i][6]}     Course 3: {details[i][7]}     Course 4: {details[i][8]}     Course 5: {details[i][9]}     Course 6: {details[i][10]}")
            detailsList.insert(tk.END, " ")
        
        detailsList.pack(side = "right", fill = "both")
        scrollbar1.config(command = detailsList.yview)
        scrollbar2.config(command = detailsList.xview)

        viewButtonFrame = tk.Frame(self,bd= 0, relief = "raised")
        viewButtonFrame.place(x = 250, y = 50, width = 1000, height = 50)
        refreshButton = tk.Button(viewButtonFrame, text = "Refresh", width = 28, bg = "dark turquoise", font = Small_Font, command = refreshPage)
        refreshButton.pack(side = "top", pady = 10, padx = 10, anchor = "ne")

        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Student Management", width = 28, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StudentManagement))
        backButton.pack(side = "bottom", pady = 10, padx = 10)


class EnterMarks(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text = "Enter Marks(Percentage)", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        rollFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        rollFrame.place(x = 80, y = 40, width = 1300, height = 80)
        rollno = tk.Label(rollFrame, text = "Enter Rollno: ", font = Large_Font, bg = "dark turquoise")
        rollno.grid(row = 0, column= 0, padx = 50, pady = 20)
        rollnoEntry = tk.Entry(rollFrame, width = 30, font = Large_Font)
        rollnoEntry.grid(row = 0, column= 1, padx = 50, pady = 20)

        inputFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        inputFrame.place(x = 40, y = 150, width = 1400, height =500)

        marks_course1 = tk.Label(inputFrame, text = "Course 1: ", font = Large_Font, bg = "dark turquoise")
        marks_course1.grid(row = 1, column= 0, padx = 80, pady = 20)
        marks_course1_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course1_Entry.grid(row = 1, column= 1, padx = 80, pady = 20)

        marks_course2 = tk.Label(inputFrame, text = "Course 2: ", font = Large_Font, bg = "dark turquoise")
        marks_course2.grid(row = 2, column= 0, padx = 80, pady = 20)
        marks_course2_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course2_Entry.grid(row = 2, column= 1, padx = 80, pady = 20)

        marks_course3 = tk.Label(inputFrame, text = "Course 3: ", font = Large_Font, bg = "dark turquoise")
        marks_course3.grid(row = 3, column= 0, padx = 80, pady = 20)
        marks_course3_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course3_Entry.grid(row = 3, column= 1, padx = 80, pady = 20)

        marks_course4 = tk.Label(inputFrame, text = "Course 4: ", font = Large_Font, bg = "dark turquoise")
        marks_course4.grid(row = 4, column= 0, padx = 80, pady = 20)
        marks_course4_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course4_Entry.grid(row = 4, column= 1, padx = 80, pady = 20)
        
        marks_course5 = tk.Label(inputFrame, text = "Course 5: ", font = Large_Font, bg = "dark turquoise")
        marks_course5.grid(row = 5, column= 0, padx = 80, pady = 20)
        marks_course5_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course5_Entry.grid(row = 5, column= 1, padx = 80, pady = 20)

        marks_course6 = tk.Label(inputFrame, text = "Course 6: ", font = Large_Font, bg = "dark turquoise")
        marks_course6.grid(row = 6, column= 0, padx = 80, pady = 20)
        marks_course6_Entry = tk.Entry(inputFrame, width = 45, font = Large_Font)
        marks_course6_Entry.grid(row = 6, column= 1, padx = 80, pady = 20)

        def updateLabels(rollno):
            outputList = search("Databases\\student","roll number",rollno)
            marks_course1.config(text = str(outputList[4]) + ": ")
            marks_course2.config(text = str(outputList[5]) + ": ")
            marks_course3.config(text = str(outputList[6]) + ": ")
            marks_course4.config(text = str(outputList[7]) + ": ")
            marks_course5.config(text = str(outputList[8]) + ": ")
            marks_course6.config(text = str(outputList[9]) + ": ")

        showButton = tk.Button(rollFrame, text = "Search", width = 28, bg = "dark turquoise", font = Large_Font, command = lambda: updateLabels(rollnoEntry.get()))
        showButton.grid(row = 0, column= 2, padx = 50, pady = 20)
        #####Submit Button##############
        def getInput():
            Sroll = rollnoEntry.get()
            Sc1 = marks_course1_Entry.get()
            Sc2 = marks_course2_Entry.get()
            Sc3 = marks_course3_Entry.get()
            Sc4 = marks_course4_Entry.get()
            Sc5 = marks_course5_Entry.get()
            Sc6 = marks_course6_Entry.get()
            Slist = [Sroll, Sc1, Sc2, Sc3, Sc4, Sc5, Sc6]
            return Slist
        
        def deleteEntryFields():
            rollnoEntry.delete(0, tk.END)
            marks_course1_Entry.delete(0, tk.END)
            marks_course2_Entry.delete(0, tk.END)
            marks_course3_Entry.delete(0, tk.END)
            marks_course4_Entry.delete(0, tk.END)
            marks_course5_Entry.delete(0, tk.END)
            marks_course6_Entry.delete(0, tk.END)

        def addMarks():
            outputList = search("Databases\\student","roll number",rollnoEntry.get())
            if outputList[0] == "Not Available":
                messagebox.showwarning("Warning!!!", "Record Not Found!!!")
            else:
                checkList = search("Databases\\studentMarks","roll number",rollnoEntry.get())
                if checkList[0] == "Not Available":
                    entryList = getInput()
                    if "" in entryList:
                        messagebox.showwarning("Warning!!!", "No Entry field should remain empty!!!")
                    else:
                        details = {
                            "name" : [outputList[0]],
                            "department" : [outputList[1]],
                            "roll number" : [entryList[0]],
                            "course1" : [entryList[1]],
                            "course2" : [entryList[2]],
                            "course3" : [entryList[3]],
                            "course4" : [entryList[4]],
                            "course5" : [entryList[5]],
                            "course6" : [entryList[6]]
                        }
                        write_to_file(details, "Databases\\studentMarks")
                        deleteEntryFields()
                else:
                    entryList = getInput()
                    if "" in entryList:
                        messagebox.showwarning("Warning!!!", "No Entry field should remain empty!!!")
                    else:
                        details = {
                            "name" : [outputList[0]],
                            "department" : [outputList[1]],
                            "roll number": [entryList[0]],
                            "course1" : [entryList[1]],
                            "course2" : [entryList[2]],
                            "course3" : [entryList[3]],
                            "course4" : [entryList[4]],
                            "course5" : [entryList[5]],
                            "course6" : [entryList[6]]
                        }
                        modify_details("Databases\\studentMarks", entryList[0], details)
                        deleteEntryFields()

        submitButtonFrame = tk.Frame(self, bd= 0, relief = "raised", bg = "dark turquoise")
        submitButtonFrame.place(x = 40, y = 600, width = 1400, height = 60)
        submitButton = tk.Button(submitButtonFrame, text = "Submit", width = 28, bg = "dark turquoise", font = Large_Font, command = lambda: addMarks())
        submitButton.grid(row = 0, column = 0, pady = 5, padx = 500)

        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Student Management", width = 28, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StudentManagement))
        backButton.pack(side = "bottom", pady = 10, padx = 10)

class ReportCard(tk.Frame):

    rollToSave = ""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Report Card", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        rollFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        rollFrame.place(x = 80, y = 40, width = 1300, height = 80)
        rollno = tk.Label(rollFrame, text = "Enter Rollno: ", font = Large_Font, bg = "dark turquoise")
        rollno.grid(row = 0, column= 0, padx = 50, pady = 20)
        rollnoEntry = tk.Entry(rollFrame, width = 30, font = Large_Font)
        rollnoEntry.grid(row = 0, column= 1, padx = 50, pady = 20)

        inputFrame1 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        inputFrame1.place(x = 40, y = 190, width = 600, height = 450)
        
        name1 = tk.Label(inputFrame1, text = "Name: ", font = Large_Font, bg = "dark turquoise")
        name1.grid(row = 0, column= 0, padx = 10, pady = 20)
        name2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        name2.grid(row = 0, column= 1, padx = 100, pady = 20)

        dept1 = tk.Label(inputFrame1, text = "Department: ", font = Large_Font, bg = "dark turquoise")
        dept1.grid(row = 1, column= 0, padx = 10, pady = 20)
        dept2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        dept2.grid(row = 1, column= 1, padx = 100, pady = 20)

        roll1 = tk.Label(inputFrame1, text = "Roll No.: ", font = Large_Font, bg = "dark turquoise")
        roll1.grid(row = 2, column= 0, padx = 10, pady = 20)
        roll2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        roll2.grid(row = 2, column= 1, padx = 100, pady = 20)

        year1 = tk.Label(inputFrame1, text = "Year: ", font = Large_Font, bg = "dark turquoise")
        year1.grid(row = 3, column= 0, padx = 10, pady = 20)
        year2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        year2.grid(row = 3, column= 1, padx = 100, pady = 20)

        Sem1 = tk.Label(inputFrame1, text = "Semester:  ", font = Large_Font, bg = "dark turquoise")
        Sem1.grid(row = 4, column= 0, padx = 10, pady = 20)
        Sem2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        Sem2.grid(row = 4, column= 1, padx = 10, pady = 20)

        hostel1 = tk.Label(inputFrame1, text = "Hostel: ", font = Large_Font, bg = "dark turquoise")
        hostel1.grid(row = 5, column= 0, padx = 10, pady = 20)
        hostel2 = tk.Label(inputFrame1, text = "", font = Large_Font, bg = "dark turquoise")
        hostel2.grid(row = 5, column= 1, padx = 100, pady = 20)

        inputFrame2 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        inputFrame2.place(x = 820, y = 190, width = 600, height = 410)

        course1 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course1.grid(row = 0, column= 0, padx = 10, pady = 15, sticky = "w")
        
        course2 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course2.grid(row = 1, column= 0, padx = 10, pady = 15, sticky = "w")
        
        course3 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course3.grid(row = 2, column= 0, padx = 10, pady = 15, sticky = "w")
        
        course4 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course4.grid(row = 3, column= 0, padx = 10, pady = 15, sticky = "w")
       
        course5 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course5.grid(row = 4, column= 0, padx = 10, pady = 15, sticky = "w")
        
        course6 = tk.Label(inputFrame2, text = "", font = Large_Font, bg = "dark turquoise")
        course6.grid(row = 5, column= 0, padx = 10, pady = 15, sticky = "w")

        def savePDF():
            rollno = self.rollToSave
            outputList = search("Databases\\student","roll number",rollno)
            marksList = search("Databases\\studentMarks", "roll number", rollno)
            a = Admin()
            details = {
                "name" : str(outputList[0]),
                "department" : str(outputList[1]),
                "roll number": str(rollno),
                "year": str(outputList[2]),
                "hostel": str(outputList[3]),
                "course1" : str(outputList[4]),
                "course2" : str(outputList[5]),
                "course3" : str(outputList[6]),
                "course4" : str(outputList[7]),
                "course5" : str(outputList[8]),
                "course6" : str(outputList[9]),
                "marks1" : str(marksList[2]),
                "marks2" : str(marksList[3]),
                "marks3" : str(marksList[4]),
                "marks4" : str(marksList[5]),
                "marks5" : str(marksList[6]),
                "marks6" : str(marksList[7]),
                "semester" : str(a.semester)
            }
            create_pdf(details)

        saveButtonFrame = tk.Frame(self, bd = 0, relief = "raised", bg = "dark turquoise")
        saveButtonFrame.place(x = 820, y = 600, width = 600, height = 40)
        saveButton = tk.Button(saveButtonFrame, text = "Save PDF", width = 20, bg = "dark turquoise", font = Small_Font, command = savePDF)
        saveButton.pack(side = "right", padx = 5)

        def updateLabels(rollno):
            self.rollToSave = rollno
            outputList = search("Databases\\student","roll number",rollno)
            marksList = search("Databases\\studentMarks", "roll number", rollno)
            name2.config(text =  str(outputList[0]))
            dept2.config(text = str(outputList[1]))
            roll2.config(text = str(rollno))
            year2.config(text = str(outputList[2]))
            a = Admin()
            Sem2.config(text = str(a.semester))
            hostel2.config(text = str(outputList[3]))
            course1.config(text = str(outputList[4]) + ": " + str(marksList[2]))
            course2.config(text = str(outputList[5]) + ": " + str(marksList[3]))
            course3.config(text = str(outputList[6]) + ": " + str(marksList[4]))
            course4.config(text = str(outputList[7]) + ": " + str(marksList[5]))
            course5.config(text = str(outputList[8]) + ": " + str(marksList[6]))
            course6.config(text = str(outputList[9]) + ": " + str(marksList[7]))

        showButton = tk.Button(rollFrame, text = "Show Marks", width = 28, bg = "dark turquoise", font = Large_Font, command = lambda: [updateLabels(rollnoEntry.get()),rollnoEntry.delete(0, tk.END)])
        showButton.grid(row = 0, column= 2, padx = 50, pady = 20)

        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Student Management", width = 28, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StudentManagement))
        backButton.pack(side = "bottom", pady = 10, padx = 10)


class StaffManagement(tk.Frame):

    outputList = "None"
    def __init__(self, parent, controller):
        self.s = Staff()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Staff Management Page", font = Large_Font)
        label.pack(pady = 10, padx = 10)

        #####Instructions Frame####
        insFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        insFrame.place(x = 0, y = 50, width = 1480, height = 70)
        ins1 = tk.Label(insFrame, text = "1. To add a staff, enter input in all the fields and click Add.", font = Small_Font, bg = "dark turquoise")
        ins1.grid(row = 0, column = 0, sticky = "w", padx = 5, pady = 5)
        ins2 = tk.Label(insFrame, text = "2. To modify a staff, enter the college ID in the input field in left frame and enter those details which are needed to be changed and click modify.", font = Small_Font, bg = "dark turquoise")
        ins2.grid(row = 1, column = 0, sticky = "w", padx = 5, pady = 5)

        #####Input Frame###########  
        inputFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        inputFrame.place(x = 40, y = 150, width = 600, height = 450)

        name = tk.Label(inputFrame, text = "Name: ", font = Large_Font, bg = "dark turquoise")
        name.grid(row = 0, column= 0, padx = 10, pady = 10)
        nameEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        nameEntry.grid(row = 0, column= 1, padx = 10, pady = 10)
        
        dept = tk.Label(inputFrame, text = "Department: ", font = Large_Font, bg = "dark turquoise")
        dept.grid(row = 1, column= 0, padx = 10, pady = 10)
        deptEntry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        deptEntry["values"] = (
            "CSE",
            "ECE",
            "BS"
        )
        deptEntry.grid(row = 1, column= 1, padx = 10, pady = 5)
        
        collegeId = tk.Label(inputFrame, text = "CollegeID.: ", font = Large_Font, bg = "dark turquoise")
        collegeId.grid(row = 2, column= 0, padx = 10, pady = 10)
        collegeIdEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        collegeIdEntry.grid(row = 2, column= 1, padx = 10, pady = 10)
        
        email = tk.Label(inputFrame, text = "E-mail: ", font = Large_Font, bg = "dark turquoise")
        email.grid(row = 3, column= 0, padx = 10, pady = 10)
        emailEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        emailEntry.grid(row = 3, column= 1, padx = 10, pady = 10)
        
        lastCollege = tk.Label(inputFrame, text = "Last College: ", font = Large_Font, bg = "dark turquoise")
        lastCollege.grid(row = 4, column= 0, padx = 10, pady = 10)
        lastCollegeEntry = tk.Entry(inputFrame, width = 25, font = Large_Font)
        lastCollegeEntry.grid(row = 4, column= 1, padx = 10, pady = 10)

        gender = tk.Label(inputFrame, text = "Gender: ", font = Large_Font, bg = "dark turquoise")
        gender.grid(row = 5, column= 0, padx = 10, pady = 10)
        genderEntry = ttk.Combobox(inputFrame, width = 24, font = Large_Font)
        genderEntry["values"] = (
            "Male",
            "Female",
            "Other"
        )
        genderEntry.grid(row = 5, column= 1, padx = 10, pady = 5)

        address = tk.Label(inputFrame, text = "Address: ", font = Large_Font, bg = "dark turquoise")
        address.grid(row = 6, column= 0, padx = 10, pady = 10)
        addressEntry = tk.Entry(inputFrame, width = 40, font = Small_Font)
        addressEntry.grid(row = 6, column = 1, padx = 10, pady = 5)


        def getInput():
            Sname = nameEntry.get()
            ScollegeId = collegeIdEntry.get()
            Sdept = deptEntry.get()
            Semail = emailEntry.get()
            SlastCollege = lastCollegeEntry.get()
            Sgender = genderEntry.get()
            Saddress = addressEntry.get()
            Slist = [Sname, ScollegeId, Sdept, Semail, SlastCollege, Sgender, Saddress]
            return Slist
        
        def deleteEntryFields():
            nameEntry.delete(0, tk.END)
            collegeIdEntry.delete(0, tk.END)
            deptEntry.delete(0, tk.END)
            emailEntry.delete(0, tk.END)
            lastCollegeEntry.delete(0, tk.END)
            genderEntry.delete(0,tk.END)
            addressEntry.delete(0,tk.END)
        
        def addStaff():
            checkList = search("Databases\\staff","roll number",collegeIdEntry.get())
            if checkList[0] == "Not Available":
                entryList = getInput()
                if "" in entryList:
                    messagebox.showwarning("Warning!!!", "No Entry field should remain empty!!!")
                else:
                    self.s.add_staff(entryList)
                    deleteEntryFields()
            else:
                messagebox.showwarning("Warning!!!", "The College ID already exists")

        def modifyStaff():
            checkList = search("Databases\\staff","roll number",collegeIdEntry.get())
            if collegeIdEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please Enter the College ID to modify!!")
            elif checkList[0] == "Not Available":
                messagebox.showwarning("Warning!!!", "The College ID does not exist!\n Add it first")
            else:
                self.s.modify_staff(getInput())
                deleteEntryFields()

        viewButtonFrame1 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewButtonFrame1.place(x = 40, y = 600, width = 600, height = 70)
        addButton = tk.Button(viewButtonFrame1, text = "Add", font = Large_Font, width = 15, bg = "dark turquoise", command = lambda: addStaff())
        addButton.grid(row = 0, column = 1, padx = 47, pady = 10)
        modifyButton = tk.Button(viewButtonFrame1, text = "Modify", font = Large_Font, width = 15, bg = "dark turquoise", command = lambda: modifyStaff())
        modifyButton.grid(row = 0, column = 2, padx = 47, pady = 10)

        #####View Frame###############
        viewFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewFrame.place(x = 740, y = 200, width = 700, height = 350)

        def searchDetails(collegeId):
            self.outputList = search("Databases\\staff","roll number",collegeId)

        nameV1 = tk.Label(viewFrame, text = "Name: ", font = Large_Font, bg = "dark turquoise")
        nameV1.grid(row = 1, column= 0, padx = 10, pady = 6)
        nameV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        nameV2.grid(row = 1, column= 1, padx = 10, pady = 6)
        
        deptV1 = tk.Label(viewFrame, text = "Department: ", font = Large_Font, bg = "dark turquoise")
        deptV1.grid(row = 2, column= 0, padx = 10, pady = 6)
        deptV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        deptV2.grid(row = 2, column= 1, padx = 10, pady = 6)

        collegeIdV1 = tk.Label(viewFrame, text = "College ID: ", font = Large_Font, bg = "dark turquoise")
        collegeIdV1.grid(row = 3, column= 0, padx = 10, pady = 6)
        collegeIdV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        collegeIdV2.grid(row = 3, column= 1, padx = 10, pady = 6)

        emailV1 = tk.Label(viewFrame, text = "E-mail: ", font = Large_Font, bg = "dark turquoise")
        emailV1.grid(row = 4, column= 0, padx = 10, pady = 6)
        emailV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        emailV2.grid(row = 4, column= 1, padx = 10, pady = 6)

        lastCollegeV1 = tk.Label(viewFrame, text = "Last College: ", font = Large_Font, bg = "dark turquoise")
        lastCollegeV1.grid(row = 5, column= 0, padx = 10, pady = 6)
        lastCollegeV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        lastCollegeV2.grid(row = 5, column= 1, padx = 10, pady = 6)
        
        genderV1 = tk.Label(viewFrame, text = "Gender: ", font = Large_Font, bg = "dark turquoise")
        genderV1.grid(row = 6, column= 0, padx = 10, pady = 6)
        genderV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        genderV2.grid(row = 6, column= 1, padx = 10, pady = 6)

        addressV1 = tk.Label(viewFrame, text = "Address: ", font = Large_Font, bg = "dark turquoise")
        addressV1.grid(row = 7, column= 0, padx = 10, pady = 6)
        addressV2 = tk.Label(viewFrame, text = "", font = Large_Font, bg = "dark turquoise")
        addressV2.grid(row = 7, column= 1, padx = 10, pady = 6)

        def updateLabels(collegeId):
            nameV2.config(text =  str(self.outputList[0]))
            deptV2.config(text = str(self.outputList[1]))
            collegeIdV2.config(text = str(collegeId))
            emailV2.config(text = str(self.outputList[2]))
            lastCollegeV2.config(text = str(self.outputList[3]))
            genderV2.config(text = str(self.outputList[4]))
            addressV2.config(text = str(self.outputList[5]))

        searchFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        searchFrame.place(x = 740, y = 150, width = 700, height = 50)
        printquery = tk.Label(searchFrame, text = "Enter a College ID to search: " , font = Small_Font, bg = "dark turquoise")
        printquery.grid(row = 0, column= 0, padx = 5, pady = 10)
        collegeIDEntry = tk.Entry(searchFrame, width = 20)
        collegeIDEntry.grid(row = 0, column= 1, padx = 5, pady = 10)

        def searchButtonCall():
            if collegeIDEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please enter the College ID before pressing search!!!")
            else:
                searchDetails(collegeIDEntry.get())
                updateLabels(collegeIDEntry.get())

        def getIDCall():
            if collegeIDEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please enter the College ID before pressing search!!!")
            else:
                searchDetails(collegeIDEntry.get())
                detailsToId = {
                    'name' : str(self.outputList[0]),
                    'department' : str(self.outputList[1]),
                    'roll number' : str(collegeIDEntry.get()),
                    'email' : str(self.outputList[2]),
                    'last college' : str(self.outputList[3]),
                    'gender' : str(self.outputList[4]),
                    'address' : str(self.outputList[5])
                }
                idGenerator(detailsToId)
                

        searchButton = tk.Button(searchFrame, text = " Search ", width = 12, bg = "dark turquoise", font = Small_Font, command = lambda: searchButtonCall())
        searchButton.grid(row = 0, column= 2, padx = 5, pady = 10)
        getIdButton = tk.Button(searchFrame, text = "Get ID", width = 12, bg = "dark turquoise", font = Small_Font, command = lambda: getIDCall())
        getIdButton.grid(row = 0, column= 3, padx = 5, pady = 10)

        def deleteButtonCall():
            if collegeIDEntry.get() == "":
                messagebox.showwarning("Warning!!!", "Please enter the College ID and search before deleting!!!")
            else:
                deleteRecord("Databases\\staff", collegeIDEntry.get())
                searchDetails(collegeIDEntry.get())
                updateLabels(collegeIDEntry.get())
                collegeIDEntry.delete(0, tk.END)

        viewButtonFrame2 = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewButtonFrame2.place(x = 740, y = 550, width = 700, height = 70)
        deleteButton = tk.Button(viewButtonFrame2, text = "Delete", font = Large_Font, bg = "dark turquoise", width = 15, command = lambda: deleteButtonCall())
        deleteButton.grid(row = 0, column = 1, padx = 70, pady = 10)
        viewAllButton = tk.Button(viewButtonFrame2, text = "View All", font = Large_Font, bg = "dark turquoise", width = 15, command = lambda: controller.show_frame(ViewAllStaff))
        viewAllButton.grid(row = 0, column = 2, padx = 70, pady = 10)

        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Home", width = 28, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(HomePage))
        backButton.pack(side = "bottom", pady = 10, padx = 10)


class ViewAllStaff(tk.Frame):

    def __init__(self, parent, controller):
        self.s = Student()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "View All Details", font = Large_Font)
        label.pack(pady = 10, padx = 10)
        viewAllFrame = tk.Frame(self,bd= 0, relief = "raised", bg = "dark turquoise")
        viewAllFrame.place(x = 250, y = 100, width = 1000, height = 580)
        scrollbar1 = tk.Scrollbar(viewAllFrame)
        scrollbar2 = tk.Scrollbar(viewAllFrame, orient = "horizontal")
        scrollbar1.pack(side = "right", fill = 'y')
        scrollbar2.pack(side = "bottom", fill = 'x')
        totalEntries, details = get_details("Databases\\staff")
        detailsList = tk.Listbox(viewAllFrame, yscrollcommand = scrollbar1.set, xscrollcommand = scrollbar2.set, bg = "dark turquoise", width = 900, font = Small_Font)
        def refreshPage():
            detailsList.delete(0, tk.END)
            totalEntries, details = get_details("Databases\\staff")
            for i in range(1, totalEntries+1):
                detailsList.insert(tk.END, f"{i}. Name: {details[i][0]}     Dept: {details[i][1]}     College ID: {details[i][2]}     E-mail: {details[i][3]}     Last College: {details[i][4]}     Gender: {details[i][5]}     Address: {details[i][6]}")
                detailsList.insert(tk.END, " ")

        for i in range(1, totalEntries+1):
            detailsList.insert(tk.END, f"{i}. Name: {details[i][0]}     Dept: {details[i][1]}     College ID: {details[i][2]}     E-mail: {details[i][3]}     Last College: {details[i][4]}     Gender: {details[i][5]}     Address: {details[i][6]}")
            detailsList.insert(tk.END, " ")
        
        detailsList.pack(side = "right", fill = "both")
        scrollbar1.config(command = detailsList.yview)
        scrollbar2.config(command = detailsList.xview)

        viewButtonFrame = tk.Frame(self,bd= 0, relief = "raised")
        viewButtonFrame.place(x = 250, y = 50, width = 1000, height = 50)
        refreshButton = tk.Button(viewButtonFrame, text = "Refresh", width = 28, bg = "dark turquoise", font = Small_Font, command = refreshPage)
        refreshButton.pack(side = "top", pady = 10, padx = 10, anchor = "ne")

        #####Back Button##############
        backButton = tk.Button(self, text = "Back To Staff Management", width = 28, bg = "dark turquoise", font = Small_Font, command = lambda: controller.show_frame(StaffManagement))
        backButton.pack(side = "bottom", pady = 10, padx = 10)


app = MainApp()
app.mainloop()
