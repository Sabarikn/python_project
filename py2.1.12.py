def group(l,s):
  i=0
  r=[]
  while i+s <= (len(l)-1):
    r.append(l[i:i+s])
    i+=s
  r.append(l[i:])
  return r
print group([1,2,3,4,5,6,7,8,9],3)
print group([1,2,3,4,5,6,7,8,9],4)

