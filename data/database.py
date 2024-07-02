from pymongo import MongoClient

class SparkDatabase:
    
    def __init__(self, collection_name: str, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client["spark"]
        self.collection = self.db[collection_name]

    def insert(self, document):
        insert_result = self.collection.insert_one(document)
        return insert_result.inserted_id

    def find(self, query):
        return self.collection.find_one(query)






