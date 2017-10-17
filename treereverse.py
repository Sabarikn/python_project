def tree_reverse(L):
  result=[]
  for l in L:
    if isinstance(l,list):
      result.insert(0,tree_reverse(l))
    else:
      result.insert(0,l)
  return result
