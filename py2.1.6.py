def rev(l):
  n=len(l)-1
  r=[]
  for i in range(len(l)):
    r.append(l[n])
    n-=1
  return r
print rev([1,2,3,4])
print rev(rev([1,2,3,4]))
