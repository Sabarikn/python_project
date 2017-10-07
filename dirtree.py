import sys
import os
dire=os.path.abspath(sys.argv[1])

def dtre(Dire,defa=0):
  for f in os.listdir(Dire):
    if os.path.isfile(Dire+'/'+f):
      if os.listdir(Dire)[-1]!=f:
        print ('|\t'*defa)+'|--'+f
      else:
        print ('|\t'*defa)+'\--'+f
    elif (os.path.isdir(Dire+'/'+f)):
      print '|--'+f+('\n|\t'*defa)+'\n',dtre(Dire+'/'+f,defa+1)

dtre(dire)
