import sys
filename=sys.argv[1]
limit=int(sys.argv[2])
res=(open(filename,'r').readlines())
for x in res:
  if len(x) <=limit:
    print x
  elif x[limit-1]==' ':
    print x[:limit]+'\n'+x[limit:]
  else :
    print ' '.join(x[:limit].split()[:-1])+'\n '+x[:limit].split()[-1]+x[limit:]

