def anagram(L):
  A=[]
  for i in range(len(L)):
    x=[]
    x.append(L[i])
    for j in range(len(L)):
      if sorted(L[i])==sorted(L[j]) and i != j:
        x.append(L[j])
    if sorted(x) not in A:
       A.append(sorted(x))
  return A
print anagram(['eat','ate','done','tea','soup','node'])
