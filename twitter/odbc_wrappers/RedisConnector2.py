import redis


class RedisConnector2:
    """ Python-ODBC Connector for strategy 2 for implementing twitter using Redis """
    def __init__(self):
        self.connection = redis.Redis(db=2)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert_following(self, follow):
        self.connection.rpush(follow[1] + ':uid' + ':follows', follow[0])

    ## 0 = tweet ID, 1 = user ID, 2 = timestamp, 3 = text
    def insert_one(self, tweet):
        self.connection.hset(tweet[1] + ':uid' + tweet[0] + ":tid", 'text', tweet[3], 'time', tweet[2], 'user_id', tweet[1], 'tweet_id', tweet[0])
        followers = self.lrange(tweet[1] + ':uid' + ':follows')
        for i in followers:
            self.connection.rpush(i + ':uid' + ':timeline', tweet[1] + ':uid' + tweet[0] + ":tid")

    def get_timeline(self, user):
        tweets = self.lrange(user + ':uid' + ':timeline', start=-10)
        timeline_tweets = []
        for i in tweets:
            tweet_text = self.connection.hget(i, 'text')
            tweet_time = self.connection.hget(i, 'time')
            tweet_user_id = self.connection.hget(i, 'user_id')
            tweet_id = self.connection.hget(i, 'tweet_id')
            timeline_tweets.append((tweet_id, tweet_user_id, tweet_time, tweet_text))
        return timeline_tweets

    def lrange(self, key, start=0, end=-1):
        return self.connection.lrange(key, start, end)