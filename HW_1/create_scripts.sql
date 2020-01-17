CREATE TABLE IF NOT EXISTS `followers` (
  `user_id` int(8) DEFAULT NULL,
  `follows_id` int(8) DEFAULT NULL,
  KEY `index1` (`user_id`,`follows_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tweets` (
  `tweet_id` int(8) DEFAULT NULL,
  `user_id` int(8) DEFAULT NULL,
  `tweet_ts` datetime DEFAULT NULL,
  `tweet_text` text,
  KEY `idx_tweets_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;