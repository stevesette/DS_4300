import pymongo


class MongoConnector:
    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.connection['hw3']

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_file(self, filename, filedata):
        col = self.db[filename]
        col.insert_many(filedata)

    def run_query(self, collection, query):
        col = self.db[collection]
        ret = []
        for x in col.find(query):
            ret.append(x)
        return ret
