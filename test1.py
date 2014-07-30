#!/usr/bin/env python

def process(line,publish):
    l=line.split()
    user=l[4].split("(")[1].split(")")[0]
    modules=line.split(",")[0].split()[5:]
    modules=','.join(modules).split("[")[1].split("]")[0].split(",")
    #print user
    #print modules
    has=0
    i=0
    publish_has={}
    if publish == [] :
       pass
    else :
       for p in publish:
           if p.has_key(user):
             has=1
             publish_has=p
             break
           else:
             pass
           i=i+1
    if has == 0:
       d={}
       d.setdefault(user,modules)       
       publish.append(d)
    if has == 1:
       for mod in modules:
           if mod in publish_has[user]:
              pass
           else:
              publish[i][user].append(mod)
       

publish=[]
modsum=0
f=open("1","r")
#f=open("tt","r")
for line in f:
    process(line,publish)
f.close()

result={}
for ll in publish:
  #print ll.keys()[0]+",",
  #print str(len(ll.values()[0]))
  result.setdefault(ll.keys()[0],len(ll.values()[0]))
  modsum=modsum+len(ll.values()[0])
result=sorted(result.iteritems(),key=lambda asd:asd[1],reverse=True )
for r in result:
  print r[0]+"--------"+str(r[1])
  #print r[0]+",",
#print publish
#print len(publish)
#print modsum
