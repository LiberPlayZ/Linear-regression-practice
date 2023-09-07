import math
# from Utilities.draw_Graph import creating_Regression_Line_Graph_With_Marked_Points
import numpy as np
from Utilities.Linear_Regression import *


def gradient_descent(x, y):
    m_curr = 0
    b_curr = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002
    cost = 0
    cost_previous = 0
    i = 0

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([value ** 2 for value in (y - y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost

    print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))
    return m_curr, b_curr


def main():
    x = [92, 56, 88, 70, 80, 49, 65, 35, 66, 67]
    y = [98, 68, 81, 80, 83, 52, 66, 30, 68, 73]
    # x = [
    #     12,
    #     10,
    #     8,
    #     12,
    #     20,
    #     6,
    #     6
    # ]
    # y = [
    #     2, 3, 6, 0, 1, 8, 6
    # ]
    # x = [
    #     18,
    #     20,
    #     22,
    #     24,
    #     26,
    #     28
    # ]
    # y = [
    #     12,
    #     14,
    #     16,
    #     18,
    #     20,
    #     22
    # ]
    r = Linear_regression_object(x, y)
    a, b, c = r.correlation_coefficient, r.slope, r.intercept
    b2, c2 = gradient_descent(np.array(x), np.array(y))
    print(f"{a} {b} {c}")


main()
