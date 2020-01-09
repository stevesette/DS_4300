use twitter_4300;
CREATE TABLE IF NOT EXISTS twitter_4300.tweets (
	`tweet_id` long,
    `user_id` long,
    `tweet_ts` datetime,
    `tweet_text` text
    )
    ;
CREATE TABLE IF NOT EXISTS twitter_4300.followers (
	user_id long,
    follows_id long
    );