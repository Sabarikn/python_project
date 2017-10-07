def unique(l):
  r=[]
  for i in range(len(l)):
    if l[i] not in l[:i] and  l[i] not in r:
      r.append(l[i])
  return r
print unique([1,55,2,4,5,2,55,2,5,9,1,2])
