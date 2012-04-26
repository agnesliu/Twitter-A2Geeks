#######Parse Tweets from Twitter#####
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
#print members

# open file for storing source/target of retweets/mentions/replies   
out=open("retweets.txt",'w')
out.write('Source'+'\t'+'Target')

#regular expression for checking name after @
after_at=re.compile(r'@(?P<target>\w+)')

#store error message
error_log = open('error_log.txt', 'w')

sumoftweets={}
#retrieve tweets member by member
for member in members:
    print member
    try:
#       tweets=tweepy.api.user_timeline(screen_name=member,count=20)
        c = Cursor(api.user_timeline, member)
        tweets = []
        #loop until the last tweet of the page is created before 2012
        time_is_right = True
        while(time_is_right):
            print 'new page!!'
            try:
                page = c.pages().next()
                tweets.extend(page)
                month = page[-1].created_at.month
                year = page[-1].created_at.year
                print 'page\'s last tweet was created at', year, month
                if year < 2012 :
                    print 'this tweets is created ar year', year
                    time_is_right = False
            #error capture
            except StopIteration:
                print "Move to next unscanned"
                break
        print 'total tweets for', member, 'is', len(tweets)
        print 'begin to analyze!'
        time.sleep(1)
    #error capture and store log into file
    except TweepError:
        error_log.write('%s\n' %member)
        continue
    print 'total tweets', len(tweets)
    source=member
    for tweet in tweets:
        # print out format as 2012-02-10 23:14:36
        #print tweet.created_at
        month=tweet.created_at.month
        year=tweet.created_at.year
        print 'tweet was created in', year, month
        # get tweets that were create in January 2012
        if month == 1 and year == 2012:
            sumoftweets[source]=sumoftweets.setdefault(source,0)+1
            text=tweet.text
            targets=after_at.findall(text)
            for target in targets:
                out.write("\n%s\t%s" %(source,target))

#store name and number of tweets into the file sumoftweets.txt
out2=open("sumoftweets.txt",'w')
out2.write("Username"+"\t"+"Num of Tweets")
for key,value in sumoftweets.items():
    out2.write("\n%s\t%s" %(key,value))