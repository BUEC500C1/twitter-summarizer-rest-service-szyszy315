#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import keys

def get_all_tweets(screen_name):
#Twitter API credentials
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweetcontent= []
    for status in tweepy.Cursor(api.user_timeline,id=screen_name,count = 20,tweet_mode='extended').items(20):
        tweetcontent.append(status.full_text)
        print ("...{} tweets downloaded so far".format(len(tweetcontent)))


    #write tweet objects to JSON
    file = open(screen_name+'.json', 'w')
    print ("Writing tweet objects to JSON please wait...")
    json.dump(tweetcontent,file,indent = 4)
    print ("Done")
    file.close()
if __name__ == '__main__':
    get_all_tweets("@BU_Tweets")
