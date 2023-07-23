from pymongo import MongoClient
from MongoDBManager.Research import Research
from Utilities.Tools import *
from Utilities.Linear_Regression import *


class MongoDBManager:
    __instance = None

    @staticmethod
    def get_instance(database_name):
        """Static method to get the MongoDBManager instance."""
        if MongoDBManager.__instance is None:
            MongoDBManager(database_name)
        return MongoDBManager.__instance

    def __init__(self, database_name):
        """Private constructor."""
        if MongoDBManager.__instance is not None:
            raise Exception("This class is a Singleton! Use get_instance() to get the instance.")
        else:
            MongoDBManager.__instance = self
            self.client = MongoClient("mongodb://localhost:27017")
            self.db = self.client[database_name]

    def find_In_Collection(self, collection_name, query):
        """Perform a MongoDB query."""
        collection = self.db[collection_name]

        return collection.find(query)

    def collection_exist(self, Collection_name):
        collections_names = self.db.list_collection_names()
        if Collection_name in collections_names:
            return Collection_name
        else:
            return None

    def add_Research(self, Collection_name):  # the func add new research to db at specific collection.
        if self.collection_exist(Collection_name) is not None:
            collection = self.get_Collection(Collection_name)
            Id = self.get_Global_Id_Value(Collection_name)
            new_Research = Research(Id + 1)
            collection.insert_one(new_Research.__dict__)
            collection.update_one({"_id": 0}, {"$inc": {"value": 1}})
        return None

    def get_Global_Id_Value(self, Collection_name):  # the func get the global id value
        if self.collection_exist(Collection_name) is not None:
            collection = self.get_Collection(Collection_name)
            global_id = collection.find_one({"_id": 0})
            return global_id['value']
        return None

    def find_In_Collection_By_Id(self, Collection_name, Id):  # the func search specific id in specific collection
        if self.collection_exist(Collection_name) is not None:
            collection = self.get_Collection(Collection_name)
            if collection.find_one({"_id": Id}) is not None:
                return collection.find_one({"_id": Id})
        return None

    def get_Collection(self, collection_name):
        if self.collection_exist(collection_name) is not None:
            return self.db[collection_name]
        else:
            return None

    def get_Data_From_Collection(self, collection_name):
        if self.collection_exist(collection_name) is not None:
            collection = self.get_Collection(collection_name)
            return collection.find({})

    def add_Research_Data_To_Db(self, collection_name,
                                Id):  # the func adding data to exist research and update all relevant data im db
        if self.find_In_Collection_By_Id(collection_name, Id) is not None:
            collection = self.get_Collection(collection_name)
            document = self.find_In_Collection_By_Id(collection_name, Id)
            document["X_Variables"], document["Y_Variables"] = add_To_double_arrays(document["X_Variables"],
                                                                                    document["Y_Variables"])
            num_of_elements = len(document["X_Variables"])
            Linear_Object = Linear_regression_object(document["X_Variables"], document["Y_Variables"],
                                                     document["X_Name"], document["Y_Name"])
            collection.update_one({"_id": Id}, {
                "$set": {"X_Variables": document["X_Variables"], "Y_Variables": document["Y_Variables"],
                         "num_of_elements": num_of_elements,
                         "correlation_coefficient": Linear_Object.correlation_coefficient,
                         "linear_connection": Linear_Object.linear_Connection,
                         "prediction_percentage": Linear_Object.prediction_percentage,
                         "graph_data": Linear_Object.graph_data}})
            return

    def close_connection(self):
        self.client.close()
# def main():
#     g = MongoDBManager.get_instance("Linear_Regression")
#     # s = g.find_In_Collection('Research', {"_id": 1})
#     # t = g.find_In_Collection('Results', {"_id": 1})
#     # f = g.get_Collection('Research')
#     #
#     # print(g)
#     # print(s)
#     # print(t)
#     # print(f)
#
#     print(g.get_Collection('Research'))
#
#
# main()
