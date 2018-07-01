#!/usr/bin/python
# -*- coding: utf-8 -*-

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pprint import pprint

# Visit https://apps.twitter.com/ to obtain the data
#import credentials.py
import tweepy
import importlib.machinery

import sys
sys.path.insert(0, "secret")

try:
    from credentials import *
except ImportError:
    print('No Import')

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
pprint(api)
user = api.me()
pprint(user) 
#api.update_status('Hello Python Central!')
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

    
