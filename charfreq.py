
def charfreq(f1):
  ch=(open(f1,'r').read())
  d={}
  for i in range(len(ch)):
    d[ch[i]]=d.get(ch[i],0)+1
  return d
def main(filename):
   
    frequency = charfreq((filename))
    print frequency
    large=max(frequency.get(';',0),frequency.get(':',0),frequency.get('.',0))
    if large==frequency.get(';',0):
      print 'C FILE'
    elif large==frequency.get(':',0):
      print 'PYTHON FILE'
    else:
      print'TEXT FILE'

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
