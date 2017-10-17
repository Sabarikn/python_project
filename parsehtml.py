import sys
import urllib
from BeautifulSoup import BeautifulSoup
url=(sys.argv[1])
f=urllib.urlopen(url)
soup=BeautifulSoup(f.read())
for i in range(len( soup.findAll('a'))):
  print soup.findAll('a')[i]['href']
