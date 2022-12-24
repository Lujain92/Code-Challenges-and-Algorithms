import re

def repeated(s):
  '''
  function called repeated used to check the first repeated word and return it
  if no repeated word it will return no repetation
  input s:string
  output: string
  '''
  h={}
  s = re.sub(r'[^\w\s]', '', s)
  print(s)
  for i in  s.split():
    h[i]=h.get(i,0)+1
  for i in s.split():
    if h[i]>1:
      return i
  return "No Repetition"

