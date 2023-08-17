import base64

from flask import Flask, request, jsonify
from flask_cors import CORS
from frontend_service import *

app = Flask(__name__)
CORS(app)

service = Service()


# @app.route('/api/hello', methods=['GET'])  # get example
# def receive_data():
#     return greeting_data
#
#
# @app.route('/api/postest', methods=['POST'])  # post example
# def post_data():
#     data = request.get_json()
#     print(data)
#     return jsonify(data)

#
# @app.route('/api/graphUrl', methods=['GET'])  # post example
# def graph_data():
#     global graph_Id
#     result = cluster.find_In_Collection_By_Id(collection_name, graph_Id)
#     print(graph_Id)
#     # data = {"message": "Data from the backend"}
#     # combined_data = {**data, **result}
#     base64_image = base64.b64encode(result["graph_data"]).decode('utf-8')
#     result['graph_data'] = base64_image
#     return jsonify(result)


@app.route('/api/IdUrl', methods=['GET'])  # post example
def receiveGraphId():
    # ReceiveGraphId = request.get_json()
    ReceiveGraphId = int(request.args.get("imageId"))
    print(type(ReceiveGraphId))
    response = {"message": "data received "}
    Model = service.create_Model_For_Front(ReceiveGraphId)
    print(Model)
    return jsonify(Model)


if __name__ == '__main__':
    app.run(debug=True)
