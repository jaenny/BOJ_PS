import sys

num = int(sys.stdin.readline())
res = 0
L=[1,1]
if num >=3 :
  for i in range(2,num) :
    L.append(L[i-2]+L[i-1])

if num == 1 :
  print(4)
else : 
  print(L[-1]*4 + L[-2]*2)