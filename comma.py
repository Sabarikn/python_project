import sys
filename =sys.argv[1]
def comma_ecv(filen):
  return [x.strip('\n ').split(',') for x in (open(filen,'r').readlines())]
print comma_ecv(filename)

