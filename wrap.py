import sys
filename=sys.argv[1]
limit=int(sys.argv[2])
res=(open(filename,'r').readlines())
for x in res:
  if len(x) <= limit:
    print x
  else:
    print x[:limit]+'\n'+x[limit:]


