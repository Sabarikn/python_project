import re
def makslug(S):
  print re.sub(r'^\W*','',re.sub(r'\W*$','',re.sub(r'\b\W*\b','-',S)))
makslug('-!hello!world--')
    
