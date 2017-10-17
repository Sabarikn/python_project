import os
def readfiles(fnames):
  for f in fnames:
    for line in open(f):
      yield line

def printfiles(Li):
  k=0
  return sum(k+1 for l in Li if l.strip() != '' and '#' not in l)


def findfiles(directory):
  r=[]
  for fi in os.listdir(directory):
    if fi.split('.')[-1]=='py':
      r.append(directory+'/'+fi)
  lines=readfiles(r)
  print printfiles(lines)

