import sys
filename =sys.argv[1]
symbol1 = sys.argv[2]
def comma_ecv(filen,symbo):
  return [x.strip('\n ').split(symbo) for x in (open(filen,'r').readlines())]
print comma_ecv(filename,symbol)


