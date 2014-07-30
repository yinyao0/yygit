#!/usr/bin/env python


def process1(line,notify):
    time=line.split("notify")[0].split("[")[0]
    modules=line.split("notify")[1].split("[")[1].split("]")[0].split()
    #print time
    #print modules
    for mod in modules:
        notify.setdefault(mod,time)

def process2(line,publish):
    time=line.split("INFO")[0].split("[")[0]
    modules=line.split(",")[0].split()[5:]
    modules=','.join(modules).split("[")[1].split("]")[0].split(",")
    #print time
    #print modules
    for mod in modules:
      publish.setdefault(mod,time)

def cal(publish,notify,x):
    nm=int(notify[x].split()[0].split("/")[1])
    nd=int(notify[x].split()[0].split("/")[2])
    nh=int(notify[x].split()[1].split(":")[0])
    nmi=int(notify[x].split()[1].split(":")[1])
    ns=int(notify[x].split()[1].split(":")[2])

    pm=int(publish[x].split()[0].split("/")[1])
    pd=int(publish[x].split()[0].split("/")[2])
    ph=int(publish[x].split()[1].split(":")[0])
    pmi=int(publish[x].split()[1].split(":")[1])
    ps=int(publish[x].split()[1].split(":")[2])
    
    nms={1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334}[nm-1]*24*3600
    nds=(nd-1)*24*3600
    nhs=nh*3600
    nmis=nmi*60
    nss=ns
    nsum=nms+nds+nhs+nmis+nss
    #print nsum
 
    pms={1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334}[pm-1]*24*3600
    pds=(pd-1)*24*3600
    phs=ph*3600
    pmis=pmi*60
    pss=ps
    psum=pms+pds+phs+pmis+pss
    #print psum
    ss=psum-nsum
    date=ss/86400
    hour=(ss-date*86400)/3600
    minute=(ss-date*86400-hour*3600)/60
    second=ss-date*86400-hour*3600-minute*60
    print x+":"+str(date)+"day"+str(hour)+"hour"+str(minute)+"minute"+str(second)+"second"+":"+"total seconds "+str(ss)

notify={}
publish={}

f1=open("3","r")
for line in f1:
  process1(line,notify)
f1.close()

f2=open("1","r")
for line in f2:
  process2(line,publish)
f2.close()
#for x in notify:
#  print #x
#print len(notify)
#for y in publish:
#  print publish[y]
#print len(publish)
for x in notify:
   if x in publish:
       cal(publish,notify,x)
       #print publish[x]
       #print notify[x]
      

