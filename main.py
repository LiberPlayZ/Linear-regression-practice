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
        print(ValueError.__name__)
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
        return f"There is not a connection between {x_name} and {y_name}"
    sign = 'Positive' if r > 0 else 'Negative'
    if abs(r) < 0.3:
        return f"There is a weak and {sign} relationship between {x_name} and  {y_name}"
    elif 0.3 < abs(r) < 0.7:
        return f"There is a moderate and {sign} relationship between {x_name} and  {y_name}"
    elif 0.7 < abs(r) < 1:
        return f"There is a strong and {sign} relationship between {x_name} and  {y_name}"
    else:
        return f"There is a perfect and {sign} relationship between {x_name} and  {y_name}"


def add_new_variable_to_db():  # the function add new object to db that include 2 topic with same amount of data .
    currentId = Variable_collection.find_one({"_id": 0})
    num_of_elements = input("enter the amount of data for x and y variables : ")
    while not isInteger(num_of_elements):
        num_of_elements = input("enter the amount of data for x and y variables : ")

    X_name = input("enter the name of the first topic :   ")
    Y_name = input("enter the name of the second topic :   ")

    x_variables = []
    y_variables = []
    curX, curY = '', ''

    for i in range(int(num_of_elements)):
        curX = input(f"enter value for x{i + 1} : ")
        curY = input(f"enter value for y{i + 1} : ")
        while not isInteger(curX) or not isInteger(curY):
            curX = input(f"enter value for x{i + 1} : ")
            curY = input(f"enter value for y{i + 1} : ")
        x_variables.append(int(curX))
        y_variables.append(int(curY))

    Variable_collection.insert_one(
        {"_id": currentId['value'] + 1, "X_Name": X_name, "X_Variables": x_variables, "Y_Name": Y_name,
         "Y_Variables": y_variables, "Num_Of_Elements": int(num_of_elements)})
    Variable_collection.update_one({"_id": 0}, {"$inc": {"value": 1}})


def view_variables_in_db():  # the function print all the items in Variable collection
    variables = Variable_collection.find({})
    for variable in variables:
        if variable['_id'] > 0:
            for key, value in variable.items():
                print(f"\033[31m{key}\033[0m : {value}")
            print("")


def Linear_Regression():
    Id = input(
        "enter the id of the variable in the db you want to calculate Linear Regression (use |view| command)  : ")
    while not isInteger(Id):
        Id = input(
            "enter the id of the variable in the db you want to calculate Linear Regression (use |view| command) : ")
    while True:
        if Result_connection.find_one({"_id": int(Id)}) is not None:
            result = Result_connection.find_one({"_id": int(Id)})
            for key, value in result.items():
                print(f"\033[31m{key}\033[0m : {value}")
            print("")
            break
        else:
            result = Variable_collection.find_one({"_id": int(Id)})
            correlation_coefficient = round(Correlation_coefficient(result['X_Variables'], result['Y_Variables']), 4)
            linear_connection = Linear_relationship(correlation_coefficient, result['X_Name'], result['Y_Name'])
            Result_connection.insert_one({"_id": int(Id), "correlation_coefficient": correlation_coefficient,
                                          "linear_connection": linear_connection})


def main():
    # print(
    #     "Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression ")
    while True:
        command = input(
            'Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression : ').lower()
        if command == 'add':
            add_new_variable_to_db()
        elif command == 'view':
            view_variables_in_db()
        elif command == 'calculate':
            Linear_Regression()
        else:
            exit()


main()
