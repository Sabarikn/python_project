def unique(l,fun):
  r=[]
  for i in range(len(l)):
    if fun(l[i]) not in l[:i] and  fun(l[i]) not in l[i+1:]:
      r.append(l[i])
  return r
print unique(['python','java','Python','Java'],lambda s:s.lower())                                       
