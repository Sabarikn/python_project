def triplets(n):
  L=[]
  [L.append(sorted((x,y,z))) for x in range(1,n) for y in range(1,n) for z in range(1,n) if x+y == z if sorted((x,y,z))not in L]
  return L
print triplets(5)
