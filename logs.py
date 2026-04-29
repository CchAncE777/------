import pandas as pd
import os
import csv
import datetime

Data_Frame = pd.DataFrame
Data_Frame.columns('Id', 'pc_username', 'function_name', 'date', 'time')

def logger(func):
    def wrapper(*args):
            print(f'{os.getlogin()}-{datetime.datetime.now()}-{func.__name__}')
            result = func(*args)
            print(f'{os.getlogin()}-{datetime.datetime.now()}-{func.__name__}')
            return result
    return wrapper

@logger
def glue(*args):
    res = ''
    for i in args:
         res += i 
    return res

glue()