# Homework 2 Analysis (Jack Tonina & Steve Setteducati)
# Contributions:
RedisConnector1 - Steve\
RedisConnector2 - Jack\
followinsert.py - Steve\
utils - Steve (just moved folder)\
ReadMe Analysis - Jack/Steve (paired writing)

## NOTE
Please check the Twitter directory for all of our code since it is shared between HW1 and HW2. We thought that adjusting our directory structure for this made the most sense in a program organizational manner. It is also worth noting that all of the computer specs from HW1's analysis readme are reflected in HW2 as well. Since this was not mentioned on the assignment PDF we figured we could leave out this redundant information and make this analysis as concise and focused toward the task we were given as possible.

## **Performance Stats:**
#### Strategy 1: Construct timelines on the fly
    - Tweets Uploaded per Second: 2,972.67 (5min 36secs total)
    - Timelines Generated per Second: 139.43
    
#### Strategy 2: Post each new tweet to all followers timelines
    - Tweets Uploaded per Second: 16.43 (16 hours and 54 minutes ish total)
    - Timelines Generated per Second: 230.99
    
## **Comparing Strategy 1 & 2:**
### Comparing Inserting 1 Million Tweets
#### Overview
In comparison, Strategy 1 is incredibly superior to Strategy 2. Strategy 1 had few enough calls against the database that the speed at which we uploaded tweets was largely limited to the connection time between the Redis DB and the Python driver file. On the contrary, Strategy 2 required us to make an obscene amount of calls against the database to pre-populate it with each user's timelines. Because of how we structured our follower/following relationships in HW 1 we had to make approximately 1.5 billion calls to the database just to insert the 750,000 tweets from the Famous Accounts user bucket. 

#### Our logic for the immense number of Database Calls when Inserting 1m tweets in Strategy 2:

For each famous account, they follow 15 other famous accounts meaning that they should have 375,000 (15 * 25,000 tweets per famous account) on their timeline. We have 30 famous accounts, meaning that total tweets present on all of these 30 accounts equals 11,250,000 (30 * 375,000) total tweets on famous timelines.

For each average account, they follow 20 of the famous accounts along with 100 other average accounts meaning that they should have 525,000 tweets on each of their timelines (20 famous accounts * 25,000 tweets + 100 average accounts * 250 tweets) on their timelines. We have 900 average accounts, meaning that total tweets present on all of these 900 accounts equals 472,500,000 (900 * 525,000) total tweets on average timelines.

For each news source account, they follow all 30 of the famous accounts meaning that they should have 750,000 (30 * 25,000 tweets per famous account) on their timeline. We have 1,250 news source accounts, meaning that total tweets present on all of these 1,250 accounts equals 937,500,000 (1,250 * 750,000) total tweets on news source timelines.

This means that the sum of all tweets on every single of our users timelines is equal to 1,421,250,000, which is how many times we need to hit the database in order to insert 1 million tweets by updating each user's timeline according to who they follow.

### Comparing Pulling Timelines
#### Overview
In comparison, Strategy 2 is twice as fast as Strategy 1. This is because all of the frontloaded computation that occurs during insertion for Strategy 2. In Strategy 1, this computation takes place during the generation of timelines. Our results for Strategy 1 and 2 also highly indicate that it depends on which user id is being randomly generated for timeline retrieval, as the timeline of a news source user will take significantly longer than the timeline of a famous user due to the number of tweet ids in their key:value store. We still feel that this best represents the actual use case of Twitter, as the logic for following/follower relationships are most accurately represented here rather than a random distribution. However, neither of these strategies even come close to keeping up with the pace required of them to keep up with Twitter's load demands. Granted, this is being run locally on a Macbook Pro 12 from 2015 and not any sort of server with high ram and better processors, nor is it being distributed over a cloud service to process these requests in parallel. We tried www.getmoreram.com to download more ram but it may not have worked.

## **Comparing Redis to MySQL:**
Both Strategy 1 and Strategy 2 destroyed MySQL's speeds for retrieving timelines. Strategy 1 at 139 timelines per second, and Strategy 2 at 230 timelines per second were far superior to MySQL's top speed of 0.597 timelines per second. In terms of insertions, the comprable MySQL strategy inserted 2,343 tweets/second which was slightly inferior to Strategy 1's 2,972 tweets/second but vastly outperformed Strategy 2's attrocious 16 tweets/second. However, we understand this factors in the time it takes to build all of the timelines for retrieval later and with our follower/following breakdown as well as our tweet assumptions, these times make sense.

### Overall
Overall, we know that Strategy 2 should be what we support, but we can't. It is just way to slow in terms of uploading tweets to even comprehend the thought of endorsing this strategy. The MySQL strategy is also gravely flawed in terms of reading timelines and therefore we cannot support it either. Strategy 1 is the best we experienced in practice and we hope, wish, and pray for whoever has to pay Twitter's server costs.

## Potential Changes in Hindsight
Our initial assumptions may have been a little ambitious. The follower/following relationships as well as the breakdown of how many users in each bucket could have been shifted to a more even ratio between the 3 buckets. This likely would have seen a drastically improved performance for Strategy 2 and something more akin to what the expected outcome is on the grading end of this assignment. Even decreasing the number of tweets from famous accounts by 5,000 to 20,000 tweets each and increasing the amount ofd times the average user tweets would have drastic changes on the number of database calls made per insertion. In addition, changing the number of users and their distribution of follower/following relationships could also improve the performance. With that said, we truly believe that our initial assumptions were reasonable enough and backed by sufficient evidence and research in our daily Twitter use to affirm our beliefs.
