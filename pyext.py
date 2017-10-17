import os
def num(L):
  c=0 
  return sum(c+ 1 for f in L if f.split('.')[-1]=='py')
def findnumpy(D):
  cnt=num(os.listdir(D))
  print cnt
