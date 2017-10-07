def invertdict(D):
  print locals()
  return {D[i]:i for i in D.keys()}
C={'x':1,'y':2,'z':3}
print invertdict(C)
