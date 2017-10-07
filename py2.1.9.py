def cumulative_product(l):
  r=[]
  p=1
  for x in l:
    p *=x
    r.append(p)
  return r
print cumulative_product([1,2,3,4,5])
print cumulative_product([5,4,3,2,1])
