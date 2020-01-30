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
    with open(filepath, "r") as infile:
        reader = csv.reader(infile)
        return [x for x in reader]


# Uploads all tweets, tracking time from start to finish
def upload_all_tweets(db_conn, tweets):
    with db_conn() as db:
        start = dt.datetime.now()
        for tweet in tweets:
            db.insert_one(tweet)
        return len(tweets) / (dt.datetime.now() - start).total_seconds()


def main():
    db_type = pick_db()
    start_read = dt.datetime.now()
    tweets = read_tweets("tweets.csv")[1:]
    reading_time = (dt.datetime.now() - start_read).total_seconds()
    print(
        f"It took {reading_time} to read 1 million tweets which means it has a rate of {len(tweets)/reading_time}"
    )
    print(upload_all_tweets(db_type, tweets))


if __name__ == "__main__":
    main()
