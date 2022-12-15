import re

def l(s):
  h={}
  s = re.sub(r'[^\w\s]', '', s)
  print(s)
  for i in  s.split():
    h[i]=h.get(i,0)+1
  for i in s.split():
    if h[i]>1:
      return i
  return 'no repeattion'
