def extsort(l):
  l.sort(key=lambda s:s.split('.')[1])
  return l
print extsort(['a.c','a.py','b.py','bar.txt','foo.txt','x.c'])
