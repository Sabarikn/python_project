import sys
option=sys.argv[1]
filename=sys.argv[2]
res=(open(filename,'r').readlines())
if len(res)<10:
  print ''.join(res)
elif option =='head':
  print ''.join(res[:10])
elif option == 'tail':
  print ''.join(res[-1:-11:-1])

