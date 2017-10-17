import sys
import inspect
mod=sys.argv[1]

imp1=__import__(mod)
print 'DESCRIPTION:\n-------',imp1.__doc__,'\nFUNCTIONS\n---------\n'
for y in dir(imp1):
  print imp1.y.__doc__
