import redis


class RedisConnector2:
    """ Python-ODBC Connector for strategy 2 for implementing twitter using Redis """
    def __init__(self):
        self.connection = redis.Redis(db=2)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_one(self, tweet):
        pass

    def get_timeline(self, user):
        pass
