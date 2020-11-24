from Supporting_Programs.databaseSS import *

class Staff:

    name = ""
    dept = ""
    collegeId = ""
    email = ""
    lastCollege = ""
    gender = ""
    address = ""
    
    def add_staff(self, inputList):
        '''
        Function to add name and Roll no. of New Student.
        '''

        self.name = inputList[0]
        self.dept = inputList[2]
        self.collegeId = inputList[1]
        self.email = inputList[3]
        self.lastCollege = inputList[4]
        self.gender = inputList[5]
        self.address = inputList[6]
        
        details = self.compress_to_dictionary()
        write_to_file(details, "Databases\\staff")

    def listCheck(self,a,b):
        '''
        function to check what is in a and b and return whichever is not empty
        '''

        if b == "":
            return a
        else:
            return b

    def modify_staff(self, inputList):
        '''
        Function to modify staff details.
        '''
        prevInput = search("Databases\\staff","roll number", inputList[1])
        self.name = self.listCheck(prevInput[0], inputList[0])
        self.dept = self.listCheck(prevInput[1], inputList[2])
        self.collegeId = inputList[1]
        self.email = self.listCheck(prevInput[2], inputList[3])
        self.lastCollege = self.listCheck(prevInput[3], inputList[4])
        self.gender = self.listCheck(prevInput[4], inputList[5])
        self.address = self.listCheck(prevInput[5], inputList[6])
        details = self.compress_to_dictionary()
        modify_details("Databases\\staff",inputList[1], details)

    def compress_to_dictionary(self):
        details = {
            'name' : [self.name],
            'dept' : [self.dept],
            'collegeId' : [self.collegeId],
            'email' : [self.email],
            'last college' : [self.lastCollege],
            'gender' : [self.gender],
            'address' : [self.address]
        }
        return details

