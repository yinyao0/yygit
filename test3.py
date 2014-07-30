#!/usr/bin/env python
from __future__ import division

def process(line,modules):
    module=line.split(":")[0].split("(")[0]
    time=line.split(":")[2].split()[2]
    #print module
    times=[]
    times.append(time)
    #print times
    if modules.has_key(module):
       modules[module].append(time)
    else:
       modules.setdefault(module,times)
    


modules={}
f=open("r2","r")
for line in f:
   process(line,modules)
f.close()
#for mod in modules:
#   print mod
#   print modules[mod]
result={}
for mod in modules:
   tsum=0
   for time in modules[mod]:
       tsum=tsum+int(time)
   #print tsum   
   average=tsum/len(modules[mod])/60
   average=float("%.2f"%average)
   #print mod+",",
   #print str(average)+",",
   result.setdefault(mod,average)
   #print mod+":"+str(average)
   #print result
result=sorted(result.iteritems(),key=lambda asd:asd[1],reverse=False )
for r in result:
   print ("%-55s %.2fminutes"%(r[0],r[1]))
#print len(modules)
