###Insert Twitter  Data Into Tables###
#written by Liu Liu for SI601W12 Project

import sqlite3 as lite
import sys

fhand=open("A2GeeksTwitterUsernames.txt","r")
members=[]
# check if name is in the memberlist
# add unique screenname to a list
for line in fhand:
    line=line.rstrip()
    (fullname,screenname)=line.split('\t')
    if fullname=='Name': continue
    if screenname in members: continue
    members.append(screenname)

# a list of names used for checking if screenname appears the first time
uniquename=[]    
fhand=open("retweets.txt",'r')

con = None
try:
    con = lite.connect('a2geeksTwitter.db')
    cur = con.cursor()  
    
    for line1 in fhand:
        line1=line1.rstrip()
        (source,target)=line1.split('\t')
        # skip the tile line
        if source=="Source": continue
        # if not exists, add to the table
        if not source in uniquename:
            uniquename.append(source)
            cur.execute("insert into twitterNodes(username) values(\"" + source + "\")")
        # if not exists, add to the table
        if not target in members: continue
        if target==source: continue
        if not target in uniquename:
            uniquename.append(target)
            cur.execute("insert into twitterNodes(username) values(\"" + target + "\")")
        # add edges(source,target) into table
        cur.execute("insert into twitterEdges(source,target) values(?,?)",(source,target))
    
    con.commit()
    print uniquename

except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()