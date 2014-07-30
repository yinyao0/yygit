#!/usr/bin/env python
import sys
import re

def process(nml,name):
    #return set(name).issubset(set(nml))
    nml=("/").join(nml)
    if re.match(name,nml):
      return True
    else:
      return False


if len(sys.argv)==1:
   print "******************************************************"
   print "please input 'help' for looking up the command"
   print "******************************************************"
   sys.exit(1)
else:
   cmd=sys.argv[1]
#name=str(name)
namelist=[]
f=open("r4","r")
for line in f:
    namelist.append(line)
f.close()
#print namelist
if cmd=="s":
   name=sys.argv[2]
   ttime=[]
   subnamelist=[]
   for nm in namelist:
       #print nm
       nml=nm.split(" ")[0]
       #print nml
       nml=nml.split("/")
       if process(nml,name):
          subnamelist.append(nm)
          time=float(nm.split(" ")[-1].split("m")[0])
          ttime.append(time)
   subnamelist.sort()
   for name in subnamelist:
       print name
   tsum=0.0
   for t in ttime:
       tsum=tsum+t
   if len(ttime)==0:
      print "no value"
      sys.exit(1)
   average=tsum/len(ttime)
   print "average="+str(average)+" minutes"
   print "total number :"+str(len(ttime)) 
elif cmd=="help":
     print "enjoy!   copyright by yy"
     print "******************************************************************"
     print "the commands are:"
     print "s   search the product match for the prefix input like this :app/ecom"
     print "a   print all the product"
     print "pn  print the QA published the number of modules"
     print "******************************************************************"
elif cmd=="a":
     namelist.sort()
     for nm in namelist:
         print nm
elif cmd=="pn":
     f1=open("r1","r")
     for line in f1:
         print line
     f1.close()
else:
     print "*****************************************************"
     print "please input 'help' for looking up the command" 
     print "*****************************************************"
