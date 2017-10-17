def permute(L):
  if len(L)==0 :
    return []
  if len(L)==1:
    return L
  result=[]
  for i in range(len(L)):
    per=L[i]
    rem=L[:i]+L[i+1:]
    for p in permute(rem): 
      result.append( [per]+[p])
  return result
print permute([1,2,3])
