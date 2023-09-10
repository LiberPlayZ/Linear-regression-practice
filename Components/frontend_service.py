import base64

# from flask import jsonify
from Utilities.Backend_Tools import isInteger
from MongoDBManager import MongoManager as MgDb
import environment_variables as EV


class Service:

    def __init__(self):
        self.cluster = MgDb.MongoDBManager.get_instance(EV.Database_Name)
        self.collection_name = EV.Collection_Name

    def create_graph_model_for_front(self, graph_Id):  # create graph model for frontend
        front_Model = {}
        if self.cluster.find_In_Collection_By_Id(self.collection_name, int(graph_Id)) is not None:
            result = self.cluster.find_In_Collection_By_Id(self.collection_name, int(graph_Id))
            front_Model['graph data'] = result['graph data']
            base64_image = base64.b64encode(result["graph_data"]).decode('utf-8')
            front_Model['graph_data'] = base64_image
            table_points_model = dict(X_name=result['X_Name'], X_array=result['X_Variables'],
                                      Y_name=result['Y_Name'], Y_array=result['Y_Variables'])
            front_Model['points_model'] = table_points_model
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
                                    linear_connection=variable['linear_connection'],
                                    correlation_coefficient=variable['correlation_coefficient'])
                dataList.append(current_item)
        return dataList

# def main():
#     ser = Service()
#     ser.sendListForTable()
#     print(ser.create_graph_model_for_front(1))
#
#
# main()
