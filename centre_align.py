import sys
filename=sys.argv[1]
res=(open(filename,'r').readlines())
mx=[]
for x in res:
  mx.append(len(x))
big=max(mx)
for y in res:
  print ' '*((big-len(y))//2)+y

  
