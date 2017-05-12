#!/usr/bin/python

from collections import defaultdict
import matplotlib.pyplot as plt

fr=open('part-00000-sorted','r')
degree,nodes=[],[]
helperDict=defaultdict(list)
count=0
for line in fr:
    parts=line.strip().split('\t')
    if len(parts)==2:
        node=int(parts[1])
        helperDict[node].append(parts[0])
        count+=1

for k,v in helperDict.iteritems():
    helperDict[k]=len(v)/float(count)

#print helperDict
plt.xlabel('degree')
plt.ylabel('fraction of nodes')
#print helperDict.values()

# set axes
plt.xscale('log')
plt.yscale('log')

plt.scatter(helperDict.keys(),helperDict.values())
plt.grid(True)
plt.show()
