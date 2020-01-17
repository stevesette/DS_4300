use twitter_4300;
CREATE TABLE IF NOT EXISTS twitter_4300.tweets (
	`tweet_id` int(8),
    `user_id` int(8),
    `tweet_ts` datetime,
    `tweet_text` text
    )
    ;
CREATE TABLE IF NOT EXISTS twitter_4300.followers (
	user_id int(8),
    follows_id int(8)
    );
    