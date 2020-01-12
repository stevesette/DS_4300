import mysql.connector


class MySQLConnector:
    def __init__(
        self,
        user='tweetinsertuser',
        password='tweettweet',
        host="localhost",
        database="twitter_4300",
    ):
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
        )
        self.database = database
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def insert_one(self, tweet):
        insert_query = f"INSERT INTO {self.database}.tweets " \
                       f"(tweet_id, user_id, tweet_ts, tweet_text) " \
                       f"VALUES {tuple(tweet)}"
        print(insert_query)
        self.cursor.execute(insert_query, tweet)
