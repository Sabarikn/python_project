import re
import sys 
ph =sys.argv[1]
rule=re.compile(r'(^[+0-9]{0,3})([0-9]{10,11})$')
if not rule.search(ph):
  print('Invalid mobile number')
else:
  print('number validated')
