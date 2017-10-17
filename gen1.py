
import os
def gen(L,d):
  for f in L:
    if os.path.isfile(d+'/'+f):
      yield os.path.abspath(f)
    else:
      findfiles(d+'/'+f)
def printfiles(Li):
  for f in Li:
    print f
def findfiles(directory):
  files=gen(os.listdir(directory),directory)
  printfiles(files)
