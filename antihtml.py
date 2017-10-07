import urllib
import sys
import re
url=sys.argv[1]
if url[-1]=='/':
  print 'saving'+url+'as index.html'
  index=urllib.urlopen(url)
  open('index.html','w+').write(index.read())

else:
  print 'saving'+url+' as '+ url.split('/')[-1]
  index=urllib.urlopen(url)
  open('index.html','w+').write(index.read())

print (re.sub('<.*>',' ', open('index.html','r').read()))
