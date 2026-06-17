import re
import multiprocessing
import random

list_number = list(random.sample(range(100, 1000), 500))
list_number1 = str(list_number)

def writing():
    with open('our_numbers.csv', 'w') as num:
        num.write(list_number1)
    print('')

def reading():
    with open('our_numbers.csv', 'r') as num1:
        a = num1.read()
        a.strip()
        a.split(',')
    return a

def func_for_process(list1: list):
    num = 1
    for i in list1:
        num *= i

    return num

a = reading()

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

counter = 100

def for_list():
    counter = 100
    global a
    list1 = []
    while counter:
        if counter > 0:
            list1.append(0)
            a.remove(0)
            counter -= 1
        else:
            return list1
        
list1 = for_list()

 