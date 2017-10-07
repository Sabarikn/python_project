import urllib
import sys
url=sys.argv[1]
if url[-1]=='/':
  print 'saving'+url+'as index.html'
  index=urllib.urlopen(url)
  open('index.html','w+').write(index.read())
 
else:
  print 'saving'+url+' as '+ url.split('/')[-1]
  index=urllib.urlopen(url)
  open(url.split('/')[-1],'w+').write(index.read())
