def min1(l):
  mi=l[0]
  for x in l:
    if x <= mi:
      mi=x
  return mi

def max1(l):
  ma=l[0]
  for x in l:
    if x >= ma:
      ma=x
  return ma

print min1([5,6,4,5,13,6,3])
print min1(['hel','lo','wor','ld'])
print max1([5,6,4,5,13,6,3])
print max1(['hel','lo','wor','ld'])

