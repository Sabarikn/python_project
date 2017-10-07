def sum1(l):
  if type(l[0]) == str:
      su=''
  else:
      su=0
  print su
  for e in l:
    su += e
  return su
print sum1([1,5,6,2,6])
print sum1(['hello','worlds'])


