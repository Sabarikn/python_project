def cumulative_sum(l):
  r=[]
  s=0
  for x in l:
    s+=x
    r.append(s)
  return r
print cumulative_sum([1,2,3,4,5])
print cumulative_sum([5,4,3,2,1])
