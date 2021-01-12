from math import *
L=[]
m=int(input()); n=int(input())

while(m<=n) :
  if sqrt(m) == int(sqrt(m)) :
    L.append(m)
  m+=1
if len(L)==0 :
  print(-1)
else :
  print(sum(L))
  print(min(L))
