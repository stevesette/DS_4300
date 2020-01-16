from csv import writer
from datetime import datetime as dt
import random
import string
import randomtimestamp

# ACCOUNT GENERATOR

# 1,000,000 tweets
# famous = 25,000 (25,000 * 30 = 750,000)
# average = 250 (250 * 900 = 225,000
# newsSource = 20 (20 * 1250 = 25,000)

users = []
for i in range (2180):
    username = i
    users.append(username)

famousAccounts = []
averageAccounts = []
newsSourceAccounts = []

famousAccounts = users[:30]
print(famousAccounts)
print(len(famousAccounts))
averageAccounts = users[30:930]
print(averageAccounts)
print(len(averageAccounts))
newsSourceAccounts = users[930:]
print(newsSourceAccounts)
print(len(newsSourceAccounts))

with open('following.csv', 'w') as outfile:
    csv_writer = writer(outfile, delimiter=',', quotechar='"')
    csv_writer.writerow(['user', 'follows'])
    for i in famousAccounts:
        following = random.sample(famousAccounts,15)
        for k in following:
            csv_writer.writerow([i,k])
    for i in averageAccounts:
        following = random.sample(averageAccounts,100)
        following = following + random.sample(famousAccounts,20)
        for k in following:
            csv_writer.writerow([i,k])
    for i in newsSourceAccounts:
        following = famousAccounts
        for k in following:
            csv_writer.writerow([i,k])

# TWEET GENERATOR
start = dt.now()
with open('tweets.csv', 'w') as outfile:
    csv_writer = writer(outfile, delimiter=',', quotechar='"')
    csv_writer.writerow(['tweet_id','user_id', 'tweet_ts', 'tweet_text'])
    for i in famousAccounts:
        for k in range(25000):
            randomTweet = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(45)])
            time = randomtimestamp.randomtimestamp(start_year = 2006)
            timestamp = time[6:10] + '-' + time[3:5] + '-' + time[0:2] + ' ' + time[11:]
            tweet_id = k
            csv_writer.writerow([tweet_id, i, timestamp,randomTweet])
    for i in averageAccounts:
        for k in range(250):
            randomTweet = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(45)])
            time = randomtimestamp.randomtimestamp(start_year=2006)
            timestamp = time[6:10] + '-' + time[3:5] + '-' + time[0:2] + ' ' + time[11:]
            tweet_id = k+750000
            csv_writer.writerow([tweet_id, i, timestamp, randomTweet])
    for i in newsSourceAccounts:
        for k in range(20):
            randomTweet = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(45)])
            time = randomtimestamp.randomtimestamp(start_year=2006)
            timestamp = time[6:10] + '-' + time[3:5] + '-' + time[0:2] + ' ' + time[11:]
            tweet_id = k+975000
            csv_writer.writerow([tweet_id, i, timestamp, randomTweet])
    print('done')
writing_time = (dt.now() - start).total_seconds()
print(f"It took {writing_time} to write 1 million tweets which is an optimal rate of {writing_time/1000000}")
