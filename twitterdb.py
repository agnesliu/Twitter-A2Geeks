###Create Database And Tables###
#written by Liu Liu for SI601W12 Project

import sqlite3 as lite
import sys

import oauth2 as oauth

con = None
try:
    #check if databases a2geeksTwitter already exists
    con = lite.connect('a2geeksTwitter.db')
    cur = con.cursor()  
    #create two tables twitterEdges & twitterNodes
    cur.execute("CREATE TABLE twitterEdges(uniqueID INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, target TEXT)")   
    cur.execute("CREATE TABLE twitterNodes(uniqueID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT)")     
    con.commit()
    
          
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()