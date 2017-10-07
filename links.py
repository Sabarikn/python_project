import urllib
import sys
import re
url=sys.argv[1]
if url[-1]=='/':
  print 'saving'+url+'as index.html'
  index=urllib.urlopen(url)

else:
  print 'saving'+url+' as '+ url.split('/')[-1]
  index=urllib.urlopen(url)
 

print '\n'.join(re.findall(r'"http.*?"',index.read()))
