from MongoDBManager import MongoManager as MgDb
from Utilities.Frontend_Tools import *
import environment_variables as EV

cluster = MgDb.MongoDBManager.get_instance(EV.Database_Name)
collection_name = EV.Collection_Name


# global_id={"_id":0,"name":"global Id","value":0} # insert global variable to know number of variable inserted
# Research_collection.insert_one(global_id)


def view_variables_in_db():  # the function print all the items in Variable collection
    variables = cluster.get_Data_From_Collection(collection_name)
    for variable in variables:
        if variable['_id'] > 0:
            print_Research_From_Db(variable, False)


def show_Linear_Regression():
    Id = only_integer_input(
        'enter the id of the Research in the db you want to calculate Linear Regression (use |view| command)  :')
    if cluster.find_In_Collection_By_Id(collection_name, int(Id)) is None:
        print(
            " \033[31mThere is no  _id in the database, press|view| to see the variables or |add| to add new variable\033[0m .\n ")
        return
    else:
        result = cluster.find_In_Collection_By_Id(collection_name, int(Id))
        print_Research_From_Db(result, True)


def add_Data_To_Research():  # the func add new data to exist research and changing all relevant information.
    Id = only_integer_input('enter the id of the Research in the db you want to add data(use |view| command)  :')
    if cluster.find_In_Collection_By_Id(collection_name, int(Id)) is None:
        print(
            " \033[31mThere is no  _id in the database, press|view| to see the variables or |add| to add new variable\033[0m .\n ")
        return
    else:
        cluster.add_Research_Data_To_Db(collection_name, int(Id))


def main():
    # print(
    #     "Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression ")
    while True:
        command = input(
            'Welcome , press |add| to add new variable , |view| to show all variable in db , |calculate| for Linear regression and graph, |data| for add data : ').lower()
        if command == 'add':
            cluster.add_Research(collection_name)
        elif command == 'view':
            view_variables_in_db()
        elif command == 'calculate':
            show_Linear_Regression()
        elif command == 'data':
            add_Data_To_Research()
        else:
            cluster.close_connection()
            exit()


main()
