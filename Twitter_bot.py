# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:06:45 2020

@author: micha
"""
import tweepy
#import Requests
#import numpy as np
#import base64

print("This is my twitter bot")

CONSUMER_KEY = 'iLJwXLlqqQCR7Zf42WQJ6LTLX'
CONSUMER_SECRET = 'YQ3wpOi0IFOJLjDDgBmY0cffICmJgRma0bH6jvWQWG0rpLITP0'
ACCESS_KEY = '1020288135836635137-yDh4FQD5R5opuuA1cZCMeGDJDJAStz'
ACCESS_SECRET = 'iILDcEbMfgFCEz3eZdwajlX7F88M6eDRBrLZqWnccfjqA'

# setting up object auth and api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#type(elons_tweet) --> class <'tweepy.models.ResultSet'>
#elons_tweet[0]
# type(elons_tweet[0]) --> <class 'tweepy.models.Status'>

# FILE_NAME = 'Last_seen_tweet.txt'

# methods to return last seen tweet id from txt file
#def retrieve_Last_seen_tweet(file_name):
 #   file_read = open(file_name, 'r')
  #  Last_seen_tweet = int(file_read.read().strip())
   # file_read.close()
    #return Last_seen_tweet

#def store_Last_seen_tweet(Last_seen_tweet, file_name):
 #   file_write = open(file_name, 'w')
  #  file_write.write(str(Last_seen_tweet))
   # file_write.close()
    #return

#Last_seen_tweet = retrieve_Last_seen_tweet(FILE_NAME)

#create object elon using user ID
#elon_id = api.lookup_users(44196397)

elons_tweet = api.user_timeline(44196397,) #Last_seen_tweet)

print(elons_tweet)

# CONVERTS elons_tweet OBJECT TO DICTIONARY AND EXTRACT KEYS
elons_tweet[0].__dict__.keys()

    #pulls tweet id from dictionary so that the tweet can be retweeted
elons_tweet_id = elons_tweet[0].id

    #reweets elon musks tweet

api.retweet(elons_tweet_id)
    
    #n = n+1

# while True:
    #reply_to_tweets()
    #time.sleep(2)

