import mysql.connector


class MySQLConnector:
    def __init__(
        self,
        user,
        password,
        host="127.0.0.1",
        database="tweets_4300",
    ):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
        )

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
