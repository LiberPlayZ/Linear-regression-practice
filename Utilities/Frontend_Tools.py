import io

from PIL import Image

from Utilities.Backend_Tools import isInteger


def open_byte_as_image(data):  # the func take image byte code and show the image as png file.
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


def only_integer_input(message):  # the func gets message to show and  input only integer.
    Id = input(message)
    while not isInteger(Id):
        Id = input(message)
    return int(Id)
