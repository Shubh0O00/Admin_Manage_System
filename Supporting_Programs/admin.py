from Supporting_Programs.database import *

class Admin:
    '''
    a class to represent admin
    ...
    Attributes
    ----------
    password : str
        to store the password that is needed to start the program
        default password is shubh00
    year : str
        to store the current year in YYYY format
    name : str
        to store the name of admin
    semester : str
        to store whether the semester is odd or even

    Methods
    -------
    change_year(input_year)
        to change the current year to input_year
    change_admin(newname)
        to change the name of the admin to input name
    change_semester()
        to change the semester from odd to even and vice versa
    compress_to_dictionary()
        to create a dictionary with keys for headers of file admin.csv and values as a list of current attributes
    '''

    def __init__(self):
        details = read_database('Databases\\admin.csv')
        self.password = details['password']
        self.year = details['year']
        self.name = details['name']
        self.semester = details['semester']

    def change_year(self,newYear):
        '''
        fucntion to change the current year
        '''
        self.year = newYear
        details = self.compress_to_dictionary()
        write_database(details,'Databases\\admin.csv')

    def change_admin(self, newName):
        '''
        fucntion to change name of the admin
        '''

        self.name = newName
        details = self.compress_to_dictionary()
        write_database(details,'Databases\\admin.csv')

    def change_password(self, newPass):
        '''
        fucntion to change password
        '''

        self.password = newPass
        details = self.compress_to_dictionary()
        write_database(details,'Databases\\admin.csv')

    def change_semester(self):
        if self.semester == 'Odd':
            self.semester = 'Even'
        elif self.semester == 'Even':
            self.semester= 'Odd'
        details = self.compress_to_dictionary()
        write_database(details,'Databases\\admin.csv')

    def compress_to_dictionary(self):
        details = {
            'password' : [self.password],
            'name' : [self.name],
            'year' : [self.year],
            'semester' : [self.semester]
        }
        return details

