####GET The Influential Score for each A2GEEKS MEMBER on TWITTER in January####
#score=sum of retweets/sum of tweets
#written by Liu Liu for SI601W12 Project

from operator import itemgetter

fhand1=open("sumofretweets.txt","r")
fhand2=open("sumoftweets.txt","r")

out=open("publicscore","w")
out.write("Name"+"\t"+"Score")
#out.write("Name"+"\t"+"Score"+"\t"+"Retweet"+"\t"+"Tweet")

# get the number of retweet for each user
retweets={}
for line1 in fhand1:
    line1.rstrip()
    (name,retweet)=line1.split("\t")
    if name=="Name": continue
    retweets[name]=retweet
    
# get the number of tweets for each user
tweets={}
for line2 in fhand2:
    line2.rstrip()
    (name,tweet)=line2.split("\t")
    if name=="Username": continue
    tweets[name]=tweet
    
# compute influential score 
scores={}    
for name,retweet in retweets.iteritems():
    ret=float(retweet)
    twe=float(tweets[name])
    score=ret/twe
    scores[name]=score

# output sorted results
for name,score in sorted(scores.iteritems(),key=lambda (k,v): (v,k),reverse=True):
    out.write("\n%s\t%s" %(name,score))
    #out.write("\n%s\t%s\t%s\t%s" %(name,score,retweets[name],tweets[name]))