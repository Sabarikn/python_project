import sys
filename=sys.argv[1]
f1=open(filename,'r')
rev=f1.readlines()
print ''.join(rev[::-1])
