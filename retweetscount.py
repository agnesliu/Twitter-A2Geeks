####GET The Sum of RETWEETS for each A2GEEKS MEMBER on TWITTER in January####
#written by Liu Liu for SI601W12 Project

fhand=open("retweetsby.txt","r")

retweet={}
for line in fhand:
    line.rstrip()
    (name,num)=line.split('\t')
    num=int(num)
    if num==0: continue
    retweet[name]=retweet.setdefault(name,0)+num

out = open("sumofretweets.txt","w")   
out.write("Name"+"\t"+"Sum of Retweets")
for name,value in sorted(retweet.iteritems(),key=lambda (k,v): (v,k), reverse=True):
    out.write("\n%s\t%s" %(name,value))