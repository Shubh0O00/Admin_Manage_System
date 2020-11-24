from Supporting_Programs.databaseSS import *

class Student:
    '''
    a class to represent Students.
    ...
    Attributes
    ----------
    name : str
        To store the name of Students.
    department : str
        To store the Department(Branch) of the student.
    roll : str
        To store the Roll No. of the Student.
    year : str
        To store the year of the Student.
    cgpa : str
        To store the CGPA of the Student.
    hostel: bool
        To store whether the Student lives in Hostel or not.
        True = Yes
        False = No

    Methods
    -------
    add_student()
        To Add a Student name and roll no. in the Database.
    hostel()
	To choose if Student lives in Hostel.
    remove_student()
        To remove a Student from the Database.
    modify()
        To modify the details of a Student.
    display_cgpa()
        To display CGPA of a given Student.
    enter_courses()
        To enter courses taken by a Student.
    enter_grade()
        To enter the Grades of a Student.
    print_grade()
        To print Grades of a Student.
    display_details()
        To display the details of a Student.
    '''

    name = ""
    roll = ""
    dept = ""
    year = ""
    hostel = ""
    course1 = ""
    course2 = ""
    course3 = ""
    course4 = ""
    course5 = ""
    course6 = ""

    def add_student(self, inputList):
        '''
        Function to add name and Roll no. of New Student.
        '''

        self.name = inputList[0]
        self.roll = inputList[1]
        self.dept = inputList[2]
        self.year = inputList[3]
        self.hostel = inputList[4]
        self.course1 = inputList[5]
        self.course2 = inputList[6]
        self.course3 = inputList[7]
        self.course4 = inputList[8]
        self.course5 = inputList[9]
        self.course6 = inputList[10]
        details = self.compress_to_dictionary()
        write_to_file(details, "Databases\\student")

    def listCheck(self,a,b):
        '''
        function to check what is in a and b and return whichever is not empty
        '''

        if b == "":
            return a
        else:
            return b

    def modify_student(self, inputList):
        '''
        Function to modify student details.
        '''
        prevInput = search("Databases\\student","roll number", inputList[1])
        self.name = self.listCheck(prevInput[0], inputList[0])
        self.dept = self.listCheck(prevInput[1], inputList[2])
        self.roll = inputList[1]
        self.year = self.listCheck(prevInput[2], inputList[3])
        self.hostel = self.listCheck(prevInput[3], inputList[4])
        self.course1 = self.listCheck(prevInput[4], inputList[5])
        self.course2 = self.listCheck(prevInput[5], inputList[6])
        self.course3 = self.listCheck(prevInput[6], inputList[7])
        self.course4 = self.listCheck(prevInput[7], inputList[8])
        self.course5 = self.listCheck(prevInput[8], inputList[9])
        self.course6 = self.listCheck(prevInput[9], inputList[10])
        details = self.compress_to_dictionary()
        modify_details("Databases\\student",inputList[1], details)

    def compress_to_dictionary(self):
        details = {
            'name' : [self.name],
            'dept' : [self.dept],
            'roll' : [self.roll],
            'year' : [self.year],
            'hostel' : [self.hostel],
            'course1': [self.course1],
            'course2': [self.course2],
            'course3': [self.course3],
            'course4': [self.course4],
            'course5': [self.course5],
            'course6': [self.course6]
        }
        return details

