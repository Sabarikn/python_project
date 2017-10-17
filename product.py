def product(A,B): 
  if  B ==1:
    return A
  elif B > 1:
    return A+product(A,B-1)
  else:
    return 0
  
