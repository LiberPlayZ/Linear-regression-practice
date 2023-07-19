import io
import textwrap

import numpy as np
from matplotlib import pyplot as plt


def creating_Regression_Line_Graph_With_Marked_Points(X_Array, Y_Array, X_Name, Y_name, slope,
                                                      intercept):  # the func create linear graph image with marked points from x array and y aray

    # creating the graph
    x = np.linspace(0, max(X_Array), 100)
    y = slope * x + intercept
    fig, ax = plt.subplots()

    ax.plot(x, y, label=f'|Bx = {slope} , A = {intercept}')
    ax.scatter(X_Array, Y_Array, color='red', label='Data ')
    ax.set_xlabel(X_Name)
    ax.set_ylabel(Y_name)
    long_title = f'Regression Line between {X_Name} and {Y_name} '
    max_width = 40
    wrapped_title = textwrap.fill(long_title, max_width)
    title = ax.set_title(wrapped_title)
    plt.tight_layout()
    ax.legend()
    buffer = io.BytesIO()

    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()
    return image_data
