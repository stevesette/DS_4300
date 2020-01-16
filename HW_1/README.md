Homework 1 Analysis

Tweet Generator Assumptions:

We bucket the users of twitter into 3 general groups, famous people who tweet a lot and have many followers, normal users who follow their friends and some famous people, and people who created an account solely to follow people and probably dont tweet at all.
We modeled the numbers based on famous people (like the president), normal people (like the two of us), and made assumptions for the small bucket.
As of 1/9/2020 Donald Trump has made 50k tweets, we edited this because this is the beginning of twitter and arrived at a number of 25k tweets for the famous bucket. We also decided that famous people should take up about 3/4s of twitter, since (including retweets) we have found that this is usually the case when we use the app.
For normal people we looked at our accounts and rounded average the number of tweets we made and our following/follower ratio.
For the small bucket we imagined they just follow a few famous accounts for their source of information and maybe they write some tweets but probably not.

2. We skewed our follower percentages in a way that we thought best replicated reality. 
When timing the load for a timeline we realize that the speed for which a timeline is loaded is directly dependent on which bucket it is in. 
For instance, in an "average" user or a "news source" user we would expect the timeline to take longer to load than in a celebrity because of how many people they follow. 
This would make the join take longer and then sorting on the resulting set take longer as well. 
On the other hand the "celebrity" accounts would follow fewer people and take a shorter time to process the query.
Even though we simulate the timeline generation for 50 users because there are only 30 celebrities this result is heavily skewed in favor of accounts who follow more.
The database performance should not scale well with a higher number of either users or tweets because the inner join would require more time to complete with more records.
Similarly if the tweets were upwards of a billion or more then this issue would only get worse. 
As discussed in class, we could throw more and more resources at the database but it is unlikely that they would scale as well as we would need the product to.
What would random gen be like

3.

 