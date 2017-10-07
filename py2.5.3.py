import sys
filename=sys.argv[1]
string=sys.argv[2]
res=(open(filename,'r').readlines())
for x in res:
  if string in x:
    print x
  
  
