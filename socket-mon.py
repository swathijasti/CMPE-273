import psutil
import collections
import operator
import csv
import sys
k=psutil.net_connections()
#print k
out = []
print ("pid,laddr,raddr,status")
for i in k:
    if (i[3] and i[4]):
        out.append([i[6],i[3],i[4],i[5]])
out.sort()
#print ', '.join(['"'+i+'"' for i in out])
for i in out:
    x= i[0]
    #print i
    print i[0],i[1],i[2],i[3]
    x=i[0]
