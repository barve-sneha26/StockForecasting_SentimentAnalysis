import tweepy
import csv
import pandas as pd
import datetime
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

df = pd.DataFrame({"Dates":[],
                    "Text":[]})
tweets = []

# enter the stock name which is required for tweet data
for tweet in tweepy.Cursor(api.search_tweets, q="Infosys stocks", count=100, lang="en").items():
    print (tweet.created_at, tweet.text)

    df_temp = pd.DataFrame({"Dates":[tweet.created_at],
                    "Text":[tweet.text]})

    df=df.append(df_temp, ignore_index = True)
print(df)

df.to_csv('Infosys.csv')


