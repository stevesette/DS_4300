import pymongo


class MongoConnector:
    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.connection['hw3']

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_file(self, filename, filedata):
        col = self.db[filename]
        col['filename'].insert_many(filedata)

    def run_query(self, collection, **kwargs):
        col = self.db[collection]
        ret = []
        for x in col.find(kwargs):
            ret.append(x)
        return ret
