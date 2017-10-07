import sys
import os
dire=os.path.abspath(sys.argv[1])
print [f1 for f1 in os.listdir(dire) if os.path.isfile(dire+'/'+f1)]
