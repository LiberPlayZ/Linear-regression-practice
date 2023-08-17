import base64

# from flask import jsonify
from Utilities.Backend_Tools import isInteger
from MongoDBManager import MongoManager as MgDb
import environment_variables as EV


class Service:

    def __init__(self):
        self.cluster = MgDb.MongoDBManager.get_instance(EV.Database_Name)
        self.collection_name = EV.Collection_Name

    def create_Model_For_Front(self, graph_Id):
        result = self.cluster.find_In_Collection_By_Id(self.collection_name, int(graph_Id))
        keys_to_extract = ['correlation_coefficient', 'prediction_percentage', 'graph_data']
        front_Model = {key: result[key] for key in keys_to_extract}
        base64_image = base64.b64encode(result["graph_data"]).decode('utf-8')
        front_Model['graph_data'] = base64_image
        return front_Model

# def main():
#     ser=Service()
#     print(ser.getImage(1))
# main()
