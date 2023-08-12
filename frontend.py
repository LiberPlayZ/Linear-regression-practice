import base64

from flask import Flask, request, jsonify
from flask_cors import CORS
from MongoDBManager import MongoManager as MgDb
from Utilities.Frontend_Tools import *
import environment_variables as EV

cluster = MgDb.MongoDBManager.get_instance(EV.Database_Name)
collection_name = EV.Collection_Name
app = Flask(__name__)
CORS(app)

graph_Id = None


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


@app.route('/api/graphUrl', methods=['GET'])  # post example
def graph_data():
    global graph_Id
    result = cluster.find_In_Collection_By_Id(collection_name, graph_Id)
    print(graph_Id)
    # data = {"message": "Data from the backend"}
    # combined_data = {**data, **result}
    base64_image = base64.b64encode(result["graph_data"]).decode('utf-8')
    result['graph_data'] = base64_image
    return jsonify(result)


@app.route('/api/IdUrl', methods=['POST'])  # post example
def receiveGraphId():
    ReceiveGraphId = request.get_json()
    response = {"message": "data received "}
    global graph_Id
    graph_Id = int(ReceiveGraphId['data'])
    # print(graphId)
    # print(type(graphId))
    # print(graphId['data'])
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
