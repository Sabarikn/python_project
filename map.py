def map1(fun,L):
  return [fun(x) for x in L]
def square(y):return y*y
print map1(square,[1,2,3,4,5])
