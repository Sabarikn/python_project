def lensort(l):
  l.sort(key = lambda x:len(x))
  return l
print lensort(['c','pascal','fortran','rust','python','java'])
