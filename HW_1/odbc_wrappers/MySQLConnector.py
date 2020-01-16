import mysql.connector


class MySQLConnector:
    def __init__(
        self,
        user="tweetinsertuser",
        password="tweettweet",
        host="localhost",
        database="twitter_4300",
    ):
        self.connection = mysql.connector.connect(
            user=user, password=password, host=host, database=database,
        )
        self.database = database
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

    def insert_one(self, tweet):
        insert_query = (
            f"INSERT INTO {self.database}.tweets "
            f"(tweet_id, user_id, tweet_ts, tweet_text) "
            f"VALUES {tuple([int(tweet[0]),int(tweet[1]),tweet[2], tweet[3]])};"
        )
        self.cursor.execute(insert_query)
        self.connection.commit()

    def get_timeline(self, user):
        return_timeline = (
            f"SELECT t.user_id, tweet_text "
            f"FROM {self.database}.tweets t "
            f"INNER JOIN {self.database}.followers f ON t.user_id = f.follows_id "
            f"WHERE f.user_id = {user} "
            f"ORDER BY tweet_ts DESC "
            f"LIMIT 10;"
        )
        self.cursor.execute(return_timeline)
        return self.cursor.fetchall()
