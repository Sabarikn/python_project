def dups(l):
  r=[]
  for i in range(len(l)):
    if (l[i] in l[:i] or l[i]  in l[i+1:]) and l[i] not in r:
      r.append(l[i])
  return r
print dups([1,55,2,4,5,2,55,2,5,9,1,2])

