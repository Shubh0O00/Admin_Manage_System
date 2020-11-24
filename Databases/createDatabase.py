import pandas as pd
import os
from itertools import chain


def create_file(dictionary,name):
    '''
    Function to create File
    '''

    name=name+'.csv'
    with open(name, 'w') as file:
        str=(',').join(list(dictionary.keys()))
        file.write(str+'\n')
