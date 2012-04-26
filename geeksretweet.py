####GET RETWEETS for each TWEET by A2GEEKS MEMBER on TWITTER in January####
#written by Liu Liu for SI601W12 Project

import tweepy
from tweepy import TweepError
from tweepy import Cursor
import re
import time

# Twitter API
consumer_key='Your Consumer Key'
consumer_secret='Your Consumer Secret'
access_token='Your Access Token'
access_token_secret='Your Access Token Secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

# read twitter username/screenname from memberlist
fhand=open("A2GeeksTwitterUsernames.txt","r")
members=[]
for line in fhand:
    line=line.rstrip()
    (fullname,screenname)=line.split('\t')
    if fullname=='Name': continue
    if screenname in members: continue
    members.append(screenname)

# open file for storing retweets number  
out=open("retweetsby.txt",'w')

#store error message
error_log = open('error_log.txt', 'w')

#retrieve tweets member by member
for member in members:
    print member
    try:
        c = Cursor(api.user_timeline, member)
        tweets = []
        time_is_right = True
        while(time_is_right):
            try:
                page = c.pages().next()
                tweets.extend(page)
                month = page[-1].created_at.month
                year = page[-1].created_at.year

                if year < 2012 :
                    time_is_right = False
            except StopIteration:
                break
        time.sleep(1)
    #error capture and store log into file
    except TweepError:
        error_log.write('%s\n' %member)
        continue

    source=member
    for tweet in tweets:
        month=tweet.created_at.month
        year=tweet.created_at.year
        # get the number of retweets for each tweet
        retweet=tweet.retweet_count
        # get tweets that were create in January 2012
        if month == 1 and year == 2012:
            out.write("\n%s\t%s" %(source,retweet))
