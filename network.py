###Create GEXF File###

import sqlite3 as lite
import sys

from xml.dom.minidom import Document
out=open('twitternetwork.gexf','w')
# Create the document
doc = Document()

# create a GEXF element
gexfObject = doc.createElement("gexf")
gexfObject.setAttribute("xmlns", "http://www.gexf.net/1.2draft")
gexfObject.setAttribute("version", "1.2")
doc.appendChild(gexfObject)

# give it some meta data
metaObject = doc.createElement("meta")
metaObject.setAttribute("lastmodifieddate", "2012-02-14")
gexfObject.appendChild(metaObject)

#give it the title
creator = doc.createElement("creator")
metaObject.appendChild(creator)
myName = doc.createTextNode("LiuLiu")
creator.appendChild(myName)

#give it the title
description = doc.createElement("description")
metaObject.appendChild(description)
title = doc.createTextNode("SI601W12 Project-A2Geeks")
description.appendChild(title)

# create the title
graphObject = doc.createElement("graph")
graphObject.setAttribute("mode", "static")
graphObject.setAttribute("defaultedgetype", "directed")
gexfObject.appendChild(graphObject)

nodes = doc.createElement("nodes")
graphObject.appendChild(nodes)  

con = None
try:
    con = lite.connect('a2geeksTwitter.db')
    cur = con.cursor()  
    cur.execute("SELECT uniqueID,username FROM twitterNodes")
    nodes = doc.createElement("nodes")
    graphObject.appendChild(nodes)    
    # create nodes
    for row in cur:
        node = doc.createElement("node")
        id=str(row[0])
        node.setAttribute("id", id)
        node.setAttribute("label", row[1])
        nodes.appendChild(node)
    
    edges = doc.createElement("edges")
    graphObject.appendChild(edges)
    
    # create edges
    cur.execute("select uniqueID,(select uniqueID from TwitterNodes where username=source) sourceID,(select uniqueID from TwitterNodes where username=target) targetID from TwitterEdges;")
    for row in cur:
        if row[2]:
            edge = doc.createElement("edge")
            tid=str(row[0])
            sid=str(row[1])
            tgid=str(row[2])
            edge.setAttribute("id", tid)
            edge.setAttribute("source", sid)
            edge.setAttribute("target", tgid)
            edges.appendChild(edge)

    
except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)


finally:
    if con:
        con.close()

out.write(doc.toprettyxml(encoding="UTF-8"))