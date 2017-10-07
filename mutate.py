def mutate(string):
  L=[]
  k=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  [L.append(string[:i]+x+string[i:])for x in k for i in range((len(string)))]
  [L.append(string[:i]+x+string[i+1:])for x in k for i in range((len(string)))]
  Z=[string[:i]+string[i+1:]for i in range((len(string)))] 
  [L.append(stri[:i]+j+stri[i:])for j in k  for stri in Z for i in range((len(Z))) ]
  [L.append(string[:i]+string[i+1:]) for i in range((len(string)))] 
  return L
