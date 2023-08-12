from Utilities.Backend_Tools import create_double_arrays
from Utilities.Linear_Regression import *


class Research:
    def __init__(self, Id):
        self._id = Id
        self.X_Name = None
        self.X_Variables = None
        self.Y_Name = None
        self.Y_Variables = None
        self.num_of_elements = None
        self.create_Research()
        self.correlation_coefficient = None
        self.linear_connection = None
        self.prediction_percentage = None
        self.graph_data = None
        self.create_Linear_Regression()

    def create_Linear_Regression(self):
        Linear_object = Linear_regression_object(self.X_Variables, self.Y_Variables, self.X_Name, self.Y_Name)
        self.correlation_coefficient, self.linear_connection = Linear_object.correlation_coefficient, Linear_object.linear_Connection
        self.prediction_percentage = Linear_object.prediction_percentage
        self.graph_data = Linear_object.graph_data

    def create_Research(self):
        X_name = input("enter the name of the first topic :   ")
        Y_name = input("enter the name of the second topic :   ")
        x_variables = []
        y_variables = []
        x_variables, y_variables = create_double_arrays()

        self.X_Name = X_name
        self.X_Variables = x_variables
        self.Y_Name = Y_name
        self.Y_Variables = y_variables
        self.num_of_elements = len(x_variables)

# def main():
#     pass
#     # r = Research()
#     d,y=Research.create_double_arrays(
#     print(d)
#     # print(r.__str__())
#     # d = r.__dict__
#     # print(d)
#
#
# main()
