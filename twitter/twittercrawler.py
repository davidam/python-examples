import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key='2SA5WCwn2C1BwjAeLPKlSDSyt'
consumer_secret='Ic4MftMlT10kfFzZJkDpcMsBajbuWUP39X13LLSDC1ZwlO4Yby'
access_token_key='37636497-zhFylZ3WPr7V8ZWYSYDlBuz6O3ptj5dqlld8lwZtA'
access_token_secret='wszO8SeUnRgxz55Zt5Cw5G21pZw66QJbZG0Yf43lu4GPH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
