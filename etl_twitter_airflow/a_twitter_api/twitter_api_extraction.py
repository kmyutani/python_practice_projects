from datetime import datetime, timedelta
from textwrap import indent
from decouple import config
import pandas as pd
import os
import json
import tweepy
import s3fs

# ACCESS_KEY = config("T_ACCESS_TOKEN")
# ACCESS_SECRET = config("T_ACCESS_SECRET")
# CONSUMER_KEY = config("T_API_KEY")
# CONSUMER_SECRET = config("T_API_KEY_SECRET")

# ACCESS_KEY = config("T_API_KEY")
# ACCESS_SECRET = config("T_API_KEY_SECRET")
# CONSUMER_KEY = config("T_ACCESS_TOKEN")
# CONSUMER_SECRET = config("T_ACCESS_SECRET")

# twitter authentication
# auth = tweepy.OAuthHandler(ACCESS_KEY, ACCESS_SECRET)
# auth.set_access_token(CONSUMER_KEY, CONSUMER_SECRET)

# twitter authentication
auth = tweepy.OAuthHandler("XD18LKWa32D7TjZXdBNO9gnUF", "QodJSNDxqZiX2kiP2OiohM8D1Lk9GKRFT39qbGMI7Bw2qq6Odd")
auth.set_access_token("1514642315931176966-HrImyZLYYRbQivyyNQ2IN2GWLRCYSD", "CPp783NFguUupEuhYkCPXZsO3Wy7RrfH2igYnEpmSwg64")


# creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(
    screen_name='@elonmusk',
    count=10,
    include_rts=False,
    tweet_mode='extended'
)

tweet_list = []
for tweet in tweets:
    refined_tweet = {
        "user": tweet.user.screen_name,
        "text": tweet.full_text,
        "favorite_count": tweet.favorite_count,~
        "created_at": tweet.created_at
    }

    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("elonmust_twitter_data.csv")





