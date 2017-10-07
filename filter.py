def filter1(fun,L):
  return [x for x in L if fun(x)]
def even(x):return x%2==0
print filter1(even,[1,2,3,4,5,6,7,8,10])
