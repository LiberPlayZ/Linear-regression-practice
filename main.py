import pymongo
from pymongo import MongoClient
import math

cluster = MongoClient("mongodb+srv://dandosh5090:tru123QR@cluster0.vjtclwm.mongodb.net/?retryWrites=true&w=majority")
db = cluster['test']  # connect to db
Variable_collection = db['test']  # connect to collection
Result_connection = db['Results']


#
# global_id={"_id":0,"name":"global Id","value":0} # insert global variable to know number of variable inserted
# Variable_collection.insert_one(global_id)


def isInteger(x):  # the function if x is integer
    try:
        int(x)
        return True
    except ValueError:
        return False


def Standard_deviation(array):  # the func calculate the standard deviation of x/y
    return math.sqrt((sum(item ** 2 for item in array)) / len(array) - pow((sum(array) / len(array)), 2))


def Common_variance(array1, array2):  # the func calculate the common variance of x and y
    Sum = 0
    for x, y in zip(array1, array2):
        Sum += x * y
    return (Sum / len(array1)) - ((sum(array1) / len(array1)) * (sum(array2) / len(array2)))


def Correlation_coefficient(array1, array2):  # the func calculate the r of x and y using all the function
    return Common_variance(array1, array2) / (Standard_deviation(array1) * Standard_deviation(array2))


def Linear_relationship(r, x_name, y_name):  # The function returns a conclusion about the correlation coefficient.
    if r == 0:
        print(f"There is not a connection between {x_name} and {y_name}")
        return
    sign = 'Positive' if r > 0 else 'Negative'
    if abs(r) < 0.3:
        print(f"There is a weak and {sign} relationship between {x_name} and a {y_name}")
    elif 0.3 < abs(r) < 0.7:
        print(f"There is a moderate and {sign} relationship between {x_name} and a {y_name}")
    elif 0.7 < abs(r) < 1:
        print(f"There is a strong and {sign} relationship between {x_name} and a {y_name}")
    else:
        print(f"There is a perfect and {sign} relationship between {x_name} and a {y_name}")


def add_new_variable_to_db():
    pass


def view_variables_in_db():
    pass


def main():
    print(
        "Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression ")
    while True:
        command = input(
            'Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression')
        if command == 'add':
            add_new_variable_to_db()
        elif command == 'view':
            view_variables_in_db()
        elif command == 'calculate':
            # func()
            continue

        else:
            exit()
