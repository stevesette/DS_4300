import pymongo


class MongoConnector:
    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.connection["hw3"]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_file(self, filename, filedata):
        self.db[filename].insert_many(filedata)

    def run_query(self, collection, query):
        return [x for x in self.db[collection].find(query)]
