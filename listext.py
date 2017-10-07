import sys
import os
dire=os.path.abspath(sys.argv[1])
L=[f1 for f1 in os.listdir(dire) if os.path.isfile(dire+'/'+f1)]
k={}
for ex in L:
  i=ex.split('.')[-1]
  k[i]=k.get(i,0)+1
for j in k.keys():
  print j,k[j]

