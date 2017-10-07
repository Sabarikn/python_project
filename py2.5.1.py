import sys
filename=sys.argv[1]
res=(open(filename,'r').readlines())
for x in res:
  print x[::-1]
