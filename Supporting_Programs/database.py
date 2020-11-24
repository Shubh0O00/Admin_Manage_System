import pandas as pd

def write_database(details, filename):
    '''
    a function to write the details provided to it to the csv file
    ...
    Parameters
    ----------
    details : dict
        a dictionary containing the details from the object of class Admin
    filename : string
        a string containing the location and name of the file to be opened to write
    '''

    df = pd.DataFrame(details)
    df.to_csv(filename)

def read_database(filename):
    '''
    a function to write the details provided to it to the csv file
    ...
    Parameter
    ---------
    filename : string
        a string containing the location and name of the file to be opened to write
    
    Return
    ------
    details : dict
        a dictionary containing the details read from the row of the file <filename>
    '''

    df = pd.read_csv(filename)
    details = dict(df.iloc[0])
    return details