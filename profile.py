import datetime
def profile(F):  
  strt=(datetime.datetime.now())
  def g(x):
    h=F(x)
    return h
  elpse=((datetime.datetime.now())-strt)
  print 'time taken:%s'%(str(elpse))
  print F
  
