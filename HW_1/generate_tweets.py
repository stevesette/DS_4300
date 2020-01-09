from csv import writer
from datetime import datetime


with open('tweets.csv', 'w') as outfile:
    csv_writer = writer(outfile, delimiter=',', quotechar='"')
    csv_writer.writerow(['tweet_id', 'user_id', 'tweet_ts', 'tweet_text'])
    for tweet_id in range(1000000):
        user_id = tweet_id % 7
        csv_writer.writerow([tweet_id, user_id, ])

