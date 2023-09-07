from sklearn import linear_model
from MongoDBManager import MongoManager as MgDb
import environment_variables as EV
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import csv
#
# linear regression
cluster = MgDb.MongoDBManager.get_instance(EV.Database_Name)
collection_name = EV.Collection_Name
result = cluster.find_In_Collection_By_Id(collection_name, 1)

# X = np.array(result['X_Variables'])
# y = np.array(result['Y_Variables'])
#
# # Reshape X to a 2D array
# X = X.reshape(-1, 1)
#
# # Create and fit the linear regression model
# model = linear_model.LinearRegression()
# model.fit(X, y)
#
# # Make predictions for the given X values
# predicted_y = model.predict(X)
#
# # Print the coefficients (slope and intercept)
# print("Slope:", model.coef_[0])
# print("Intercept:", model.intercept_)
#
# # Visualize the data and regression line
# plt.scatter(X, y, label='Actual Data')
# plt.plot(X, predicted_y, color='red', label='Regression Line')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.show()


# linear regression for multiple variables
df = pd.read_csv("C:\יג יד הנדסת תוכנה\פרויקטנטים\Linear regression\multiple_variables.csv")
# print(df)
reg = linear_model.LinearRegression()


# reg.fit(df[['area', 'bedrooms', 'age']], df.price)
# print(reg.coef_)
# print(reg.intercept_)
# print(reg.predict([[3000, 3, 15]]))


# gradient decent


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_predicted)])
        md = -(2 / n) * sum(x(y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {} iteration {}".format(m_curr, b_curr, cost, i))

# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])
#
# gradient_descent(x,y)
