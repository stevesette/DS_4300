import pymongo


class MongoConnector:
    def __init__(self):
        self.db = pymongo.MongoClient("mongodb://localhost:27017/")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_products(self):
        pass

    def query_products(self, collection, **kwargs):
        pass

