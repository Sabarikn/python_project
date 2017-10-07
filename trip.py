import sys
import os
dire=os.path.abspath(sys.argv[1])
k=[(f1,os.stat(dire+'/'+f1)[6],os.path.getmtime(dire+'/'+f1)) for f1 in os.listdir(dire) if os.path.isfile(dire+'/'+f1)]
maxx=max([len(x) for x,y,z in k] )
for (a,b,c) in k:
  print a+' '*(maxx-len(a))+'\t'+str(b)+'\t'+str(c)
