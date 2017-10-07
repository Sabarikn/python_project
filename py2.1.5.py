def product(x):
  prod=1
  for z in x:
    prod *= z
  return prod
def fact(n):
  return product(range(1,n+1))
print fact(5)
print fact(0)
