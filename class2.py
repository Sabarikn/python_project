class reverse_iter:
  def __init__(self,l):
    self.lis=l[::-1]
  def __iter__(self):
    return self
  def next(self):
    if self.lis!=[]:
       x=self.lis[0]
       del self.lis[0]
       return x
    else:
      raise StopIteration()
