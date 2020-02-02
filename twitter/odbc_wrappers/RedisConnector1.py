import redis


class RedisConnector1:
    """ Python-ODBC Connector for strategy 1 for implementing twitter using Redis """

    def __init__(self):
        self.connection = redis.Redis(db=1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_following(self, follow):
        self.connection.rpush(follow[0] + ":uid" + ":following", follow[1])

    def insert_one(self, tweet):
        self.connection.rpush(tweet[1] + ":uid" + ":tid", tweet[0])
        self.connection.hset(
            tweet[1] + ":uid" + tweet[0] + ":tid", "text", tweet[3], "time", tweet[2]
        )

    def get_timeline(self, user):
        followings = self.lrange(user + ":uid" + ":following")
        all_tweets = []
        for following in followings:
            tweet_ids = self.lrange(following + ":uid" + ":tid")
            all_tweets.extend(
                [
                    (
                        tweet_id,
                        following,
                        self.connection.hget(
                            following + ":uid" + tweet_id + ":tid", "text"
                        ),
                        self.connection.hget(
                            following + ":uid" + tweet_id + ":tid", "time"
                        ),
                    )
                    for tweet_id in tweet_ids
                ]
            )
        all_tweets.sort(key=lambda x: x[3])
        return all_tweets[:10]

    def lrange(self, key, start=0, end=-1):
        return self.connection.lrange(key, start, end)
