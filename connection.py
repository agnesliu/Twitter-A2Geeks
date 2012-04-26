#######Compute Tweets/Retweets/Influence Score for Each Geek#####
#written by Liu Liu for SI601W12 Project

from operator import itemgetter

# read in members from a2geeks memberlist
fhand=open("A2GeeksTwitterUsernames.txt","r")
members=[]
for line in fhand:
    line=line.rstrip()
    (fullname,screenname)=line.split('\t')
    if fullname=='Name': continue
    if screenname in members: continue
    members.append(screenname)

fhand=open("retweets.txt",'r')
fhd=open("sumoftweets.txt",'r')

influence={}

# add up retweets/mentions/replies as influence score for each person
for line in fhand:
    line=line.rstrip()
    (source,target)=line.split('\t')
    if target=="Target": continue
    if not target in members:
        continue
    if target==source: continue
    # compute the num of retweeted/mentioned by others in the a2geeks memberlist
    influence[target]=influence.setdefault(target,0)+1
print influence

tweets={}
out=open("score.txt","w")
out.write("Username"+"\t"+"Num of Retweets"+"\t"+"Num of Tweets"+"\t"+"Score")

# read in number of tweets that each geek wrote in January 2012
for ln in fhd:
    ln=ln.rstrip()
    (username,numoftweets)=ln.split('\t')
    if username=="Username": continue
    tweets[username]=numoftweets

scores={}
for name,retweet in influence.iteritems():
    # check if two dictionaries have the same key/name
    if tweets.get(name):
        #change str to float for computing
        try:
            rt=float(retweet)
        except ValueError:
            retweet=None
            continue
        try:
            tw=float(tweets[name])
        except ValueError:
            tweets[name]=None
            continue
        #compute influece score: retweets devided by all tweets
        scores[name]=rt/tw

#write results into score.txt
for name,score in sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    out.write("\n%s\t%s\t%s\t%s" %(name,influence[name],tweets[name],score))
        

    
    
    
    
    
    