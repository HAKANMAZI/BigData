https://realpython.com/twitter-bot-python-tweepy/

import os
import tweepy as tw
import pandas as pd

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)





# Post a tweet from Python
#api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!

# Define the search term and the date_since date as variables
search_words = "#mektup"
date_since = "2019-10-16"


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
tweets


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="tr",
              since=date_since).items(100)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)
