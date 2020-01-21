# Homework 1 Analysis (Jack Tonina & Steve Setteducatti)

## **Tweet Generator Assumptions:**

We bucketed the users of Twitter into 3 general groups, famous people who tweet a lot and have many followers, normal users who follow their friends and some famous people, and people who created an account solely to follow people and probably dont tweet at all.
We modeled the numbers based on famous people (like the president), normal people (like the two of us), and made assumptions for the small bucket.
As of 1/9/2020 Donald Trump has made 50k tweets. We edited this because this is the beginning of Twitter and arrived at a number of 25k tweets for our famous users. We also decided that famous people should take up about 75% of Twitter's total tweets, since (including retweets) we have found that this is usually the case when we use the app.
For normal people, we looked at our accounts to determine how often we tweet, and how many people we follow. 
For the small bucket, we imagined they just follow a few famous accounts / news sources for their source of information / news, and probably do not send too many of their own tweets.

## **Follower / Followee Breakdown:**

#### Famous Accounts: 30
###### Following: 15 accounts (all famous other accounts)
###### Tweets per User: 25,000
###### Total Tweets From Famous Accounts: 750,000

#### Average Accounts: 900
###### Following: 120 accounts (100 average accounts, 20 famous accounts)
###### Tweets per User: 250
###### Total Tweets From Average Accounts: 225,000

#### News Source Accounts: 1,250
###### Following: 30 accounts (all famous accounts)
###### Tweets Per User: 20
###### Total Tweets From News Source Account: 25,000

#### Total Accounts: 2,180
###### Total Following Relationships: 145,950 (= 30 * 15 + 120 * 900 + 1250 * 30)
###### Total Tweets: 1,000,000

## **Analysis on Performance:**

#### 1:
CPU: Intel Core i5, 2.7GHz \
Number of Processors: 1 \
Number of Cores: 2 \
Hyperthreading: Available \
RAM: 8GB \
RAM Speed: Unclear, whatever the MacbookPro12,1 comes with default \
Disk: SSD (unclear on whether it is disk SSD or M2BE SSD) \

#### 2A:
We skewed our follower percentages in a way that we thought best replicated reality. 
When timing the load for a timeline we realize that the speed for which a timeline is loaded is directly dependent on which bucket it is in. 
For instance, in an "average" user or a "news source" user we would expect the timeline to take longer to load than in a celebrity because of how many people they follow. 
This would make the join take longer and then sorting on the resulting set take longer as well. 
On the other hand, the "celebrity" accounts would follow fewer people and take a shorter time to process the query.
Even though we simulate the timeline generation for 50 users, because there are only 30 celebrities this result is heavily skewed in favor of accounts who follow more.
The database performance would not scale well with a higher number of either users or tweets because the inner join would require more time to complete with more records.
Similarly if total tweets were greater than a billion, then this issue would only get worse. 
As discussed in class, we could throw more and more resources at the database but it is unlikely that they would scale as well as we would need the product to do so.

#### 2B:
Although it was not our approach, it is worth thinking about the implications of a randomly generated dataset and what that would mean for experiments.
We would expect a randomly generated system to have some form of normal distribution in terms of number of tweets and followers, with outliers on both ends of the spectrum.
This would not impact the ability for the system to write the tweets to the database as the query complexity would remain the same and only the users uploading would be affected.
However, retrieving timelines would be affected by a more normal distribution of tweets and followers. 
The different timelines retrieved would be more likely to have a smaller pool of followers which would mean it would be easier to do joins computationally.
This would allow for slightly faster load times than we experience when loading our timelines.

#### 3A:
We were able to write 13,000.86 tweets / second to a disk file compared to inserting into the database at a few different rates (depending on data types, and commit timing). 
First, we tried committing our inserts once per insert then with an incorrect set of datatypes and no indices. This resulted in a speed of 1,087 inserts / second.
We thought this was a good approach (minus the realization that we were inserting text datatypes instead of integers) because it makes sense that each user only commits an insert for themselves.
Next, we tried committing our inserts once at the end when we close the connection to the database. This resulted in a speed of 3,534 inserts / second.
This was a clear improvement and could be justified by imagining that the Twitter backend accepts inserts from a user but then batches and commits the tweets on a different system.
Once we thought we were good, we realized that MySQL does not have a "long" datatype and that our tables were accidentally initialized to text types rather than integers.
We also realized that it would make much more sense to put in an index, as it was very likely for Twitter to do so. 
While we believed that correcting the data type would help fix the speed, we also knew that adding an index would mean 
that it would take longer for the inserts to be done since the index has to be written for each line as well.
Again, we tried committing our tweets one at a time but this time with a corrected datatype and an index to write to as well and found a speed of 1,104.5 inserts / second.
Now that we saw in increase in speed, we thought we would try to do one batch commit at the end but found a speed of 2,343 inserts / second.
Our belief is that the decrease in speed here is because the singular commit at the end means that the database has to calculate a whole bunch of indexes at once while
with the individual commits the difference is negligible and may be a coincidence or the individual calculation of an index happens at the same time as the commit and
may happen concurrent with the continuation of the code.
Regardless of which of these options is closest to the actual Twitter backend, even the fastest of these attempts is a mere 27% of the ideal speed with the difference between the two being 9,466 tweets / second.
This may not be representative of Twitter's actual performance with MySQL before the switch because of hardware differences, database location differences (locally vs on a server), and the complexity of the databases themselves.
Overall, it is clear that we are not close to optimal performance. In addition, it is clear that we are not going to perform as well as the 4,000-6,000 tweets that Twitter actually receives per second.
However, since this is trying to imitate a smaller version of Twitter, with fewer users (since this is the beginning of Twitter), and slower hardware to process the data to the database, this is not too far off from a working version of Twitter.

#### 3B:
When thinking about optimal performance for reading a timeline, we compare the complex join query to the act of simply reading a line in a file. 
The first time we read the file in we found it took 5.085 seconds to read 1 million tweets.
This results in a rate of 196,668.05 tweets / second. Therefore, a timeline of 10 tweets would mean that we have an optimal performance of 19,666.81 timelines / second.
Now this is incredibly unrealistic because it assumes that the file is ordered perfectly and that the timeline we are looking for is grouped together perfectly.
This is simply not how the data is structured, but it can serve as an idealistic goal in a perfect world.
Therefore, it is realistic that there are very significant differences between the optimal performance and actual.
When we initially ran the timelines query we were trying to join columns together based on a text datatype and without any indexes.
The speed we found was 0.053 timelines / second. 
We realized that this was a horrible approach because of the lack of indexes and the attempt to join on text which is computationally more intensive than joining on an integer so we adjusted the database and tried again.
This time we found a speed of 0.597 timelines / second. This is better but still nowhere close to the 200k-300k timelines / second that Twitter would require.
Even considering that we are using a smaller scale, earlier version of Twitter with fewer users, this still does not come close to the numbers we would need to have a successful working product.
Overall, there are few places that we could improve this model aside from vertical scaling of the database which shows that MySQL would not be a good database to host Twitter on.
 
 #### Contributions:
 ODBC Wrappers - Steve \
 HW 1 Runtimes - Jack \
 ReadMe - Jack and Steve \
 Create Scripts - Steve \
 Following / Tweets .csv - Jack \
 Generate Tweets - Jack \
 Timeline - Jack \
 Tweet Insertion - Steve \
 