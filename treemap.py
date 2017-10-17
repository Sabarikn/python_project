def treemap(Func,L):
  result=[]
  for l in L:
    if isinstance(l,list):
      result.append(treemap(Func,l))
    else:
      result.append(Func(l))
  return result
