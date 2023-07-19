import io

from PIL import Image


def isInteger(x):  # the function if x is integer
    try:
        int(x)
        return True
    except ValueError:
        print(ValueError.__name__)
        return False


def open_byte_as_image(data):
    image_stream = io.BytesIO(data)
    image = Image.open(image_stream)
    image.show()


def print_Research_From_Db(document, graph_flag):
    for key, value in document.items():
        if key == 'graph_data' or key == 'prediction_percentage':
            if key == 'graph_data' and graph_flag is True:
                open_byte_as_image(value)
            if key == 'prediction_percentage':
                print(f"\033[31m{key}\033[0m : {value} %")
        else:
            print(f"\033[31m{key}\033[0m : {value}")
    print("")


def create_double_arrays():  # the func create 2 arrays of data in same length
    num_of_elements = input("enter the amount of data for x and y variables : ")
    while not isInteger(num_of_elements):
        num_of_elements = input("enter the amount of data for x and y variables : ")
    x_variables = []
    y_variables = []
    for i in range(int(num_of_elements)):
        curX = input(f"enter value for x{i + 1} : ")
        curY = input(f"enter value for y{i + 1} : ")
        while not isInteger(curX) or not isInteger(curY):
            curX = input(f"enter value for x{i + 1} : ")
            curY = input(f"enter value for y{i + 1} : ")
        x_variables.append(int(curX))
        y_variables.append(int(curY))
    return x_variables, y_variables


def add_To_double_arrays(x_variables, y_variables):  # the func  add data to exist arrays
    num_of_elements = input("enter the amount of data for x and y variables : ")
    while not isInteger(num_of_elements):
        num_of_elements = input("enter the amount of data for x and y variables : ")
    pos = len(x_variables)
    for i in range(int(num_of_elements)):
        curX = input(f"enter value for x{pos + 1} : ")
        curY = input(f"enter value for y{pos + 1} : ")
        while not isInteger(curX) or not isInteger(curY):
            curX = input(f"enter value for x{pos + 1} : ")
            curY = input(f"enter value for y{pos + 1} : ")
        x_variables.append(int(curX))
        y_variables.append(int(curY))
        pos += 1
    return x_variables, y_variables
