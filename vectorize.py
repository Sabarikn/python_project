def vectorise(F):
  def g(L):
    return [F(l) for l in L]
  return g
