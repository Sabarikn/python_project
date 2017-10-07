def array(x,y):
  return [[('none') for i in range(y)]for j in range(x)]
a=array(2,3)
print a
a[0][0]=5
print a
