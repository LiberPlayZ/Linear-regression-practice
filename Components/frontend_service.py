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
        front_Model = None
        if self.cluster.find_In_Collection_By_Id(self.collection_name, int(graph_Id)) is not None:
            result = self.cluster.find_In_Collection_By_Id(self.collection_name, int(graph_Id))
            keys_to_extract = ['correlation_coefficient', 'prediction_percentage', 'graph_data']
            front_Model = {key: result[key] for key in keys_to_extract}
            base64_image = base64.b64encode(result["graph_data"]).decode('utf-8')
            front_Model['graph_data'] = base64_image
        else:
            front_Model = {'correlation_coefficient': -2, 'prediction_percentage': -2, 'graph_data': 'error'}
        return front_Model

    def sendListForTable(self):  # the function takes the data from mongo and create arrays of table model for angular.
        variables = self.cluster.get_Data_From_Collection(self.collection_name)
        dataList = []
        current_item = None
        for variable in variables:
            if variable['_id'] > 0:
                current_item = dict(_id=variable['_id'], number_of_samples=variable['num_of_elements'],
                                    prediction_percentage=variable['prediction_percentage'],
                                    linear_connection=variable['linear_connection'])
                dataList.append(current_item)
        return dataList


# def main():
#     ser = Service()
#     ser.sendListForTable()
#
#
# main()
