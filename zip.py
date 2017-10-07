def zip1(X,Y):
  return [(x,y) for x in X  for y in Y if X.index(x)==Y.index(y)]
print zip1([1,2,3],['a','b','c'])
