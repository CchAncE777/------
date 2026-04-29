import os
import datetime

def func1():
    print(func1.__name__)

def func2():
    print(func2.__name__)

def func3():
    print(func3.__name__)

def func4():
    print(func4.__name__)

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

glue('awawa', 'wewewe')