import csv
import datetime as dt

from odbc_wrappers.MySQLConnector import MySQLConnector


def pick_db(mysql=True):
    if mysql:
        return MySQLConnector
    else:
        # TODO add redis connector
        return None


def read_tweets(filepath):
    with open(filepath, 'r') as infile:
        reader = csv.reader(infile)
        l = []
        for i in reader:
            l.append(i)
        return l


# Uploads all tweets, tracking time from start to finish
# took 0:15:20.633771
def upload_all_tweets(db_conn, tweets):
    # TODO figure out how this works
    with db_conn() as db:
        start = dt.datetime.now()
        for tweet in tweets:
            upload_one_tweet(db, tweet)
        return dt.datetime.now() - start


# Uploads one tweet
def upload_one_tweet(db_conn, tweet):
    db_conn.insert_one(tweet)
    return


def main():
    db_type = pick_db()
    tweets = read_tweets('tweets.csv')[1:10000000]
    print(upload_all_tweets(db_type, tweets))


if __name__ == '__main__':
    main()
