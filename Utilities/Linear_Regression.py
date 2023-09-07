import math
from Utilities.draw_Graph import creating_Regression_Line_Graph_With_Marked_Points


def Standard_deviation(array):  # the func calculate the standard deviation of x/y

    return math.sqrt((sum(item ** 2 for item in array)) / len(array) - pow((sum(array) / len(array)), 2))


def Common_variance(array1, array2):  # the func calculate the common variance of x and y
    Sum = 0
    for x, y in zip(array1, array2):
        Sum += x * y
    return (Sum / len(array1)) - ((sum(array1) / len(array1)) * (sum(array2) / len(array2)))


def Correlation_coefficient(array1, array2):  # the func calculate the r of x and y using all the function
    return Common_variance(array1, array2) / (Standard_deviation(array1) * Standard_deviation(array2))


def regression_line_Y_as_a_function_of_X(correlation_coefficient, X_Array,
                                         Y_Array):  # Regression line for predicting Y as a function of X:
    slope_Bx = (correlation_coefficient * Standard_deviation(Y_Array)) / Standard_deviation(
        X_Array)
    intercept_A = (sum(Y_Array)) / (len(Y_Array)) - (
            slope_Bx * ((sum(X_Array)) / (len(X_Array))))
    return slope_Bx, intercept_A


def regression_line_X_as_a_function_of_Y(correlation_coefficient, X_Array,
                                         Y_Array):  # Regression line for predicting X as a function of Y:
    slope_By = (correlation_coefficient * Standard_deviation(X_Array)) / Standard_deviation(
        Y_Array)
    intercept_A = (sum(X_Array)) / (len(X_Array)) - (
            slope_By * ((sum(Y_Array)) / (len(Y_Array))))
    return slope_By, intercept_A


def Linear_relationship(r, x_name, y_name):  # The function returns a conclusion about the correlation coefficient.
    if r == 0:
        return f"There is not a connection between {x_name} and {y_name}"
    sign = 'Positive' if r > 0 else 'Negative'
    if abs(r) <= 0.3:
        return f"There is a weak and {sign} relationship between {x_name} and  {y_name}"
    elif 0.3 < abs(r) <= 0.7:
        return f"There is a moderate and {sign} relationship between {x_name} and  {y_name}"
    elif 0.7 < abs(r) < 1:
        return f"There is a strong and {sign} relationship between {x_name} and  {y_name}"
    else:
        return f"There is a perfect and {sign} relationship between {x_name} and  {y_name}"


class Linear_regression_object:

    def __init__(self, X_Array, Y_Array, X_name=None, Y_Name=None):
        self.correlation_coefficient = None
        self.slope = None
        self.intercept = None
        self.prediction_percentage = None
        self.linear_Connection = None
        self.graph_data = None
        self.create_Linear_Regression_Object_With_Graph(X_Array, Y_Array, X_name, Y_Name)

    def create_Linear_Regression_Object_With_Graph(self, X_Array, Y_Array, X_name, Y_name):
        self.correlation_coefficient = Correlation_coefficient(X_Array, Y_Array)
        self.slope, self.intercept = regression_line_Y_as_a_function_of_X(self.correlation_coefficient, X_Array,
                                                                          Y_Array)

        self.prediction_percentage = ((abs(self.correlation_coefficient)) ** 2) * 100
        if X_name is not None or Y_name is not None:
            self.linear_Connection = Linear_relationship(self.correlation_coefficient, X_name, Y_name)
            self.graph_data = creating_Regression_Line_Graph_With_Marked_Points(X_Array, Y_Array, X_name, Y_name,
                                                                                self.slope, self.intercept)


# def main():
#     r = Linear_regresiion_object([18, 20, 22, 24, 26, 28], [12, 14, 16, 18, 20, 22])
#     a, b, c = r.correlation_coefficient, r.slope, r.intercept
#     print(f"{a} {b} {c}")
#
#
# main()
