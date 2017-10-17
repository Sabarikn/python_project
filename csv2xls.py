import tablib
import sys
csv=sys.argv[1]
xls=sys.argv[2]
data=tablib.Dataset()
imported=tablib.Dataset().load(open(csv).read())
with open(xls,'wd') as f:
  f.write(imported.xls)
