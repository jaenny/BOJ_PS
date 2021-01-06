#시간초과
"""
import sys

n=int(sys.stdin.readline())
cnt = 0
L=[]

for j in range(1,n+1) :
  L=[]; i=j
  while(i//10 > 0) :
    L.append(i%10)
    i=i//10
  if i//10 == 0 :
    L.append(i)
  if j % sum(L) == 0 :
    cnt += 1

print(cnt)
"""
#시간초과
"""
cnt = 0
for j in range(1,int(input())+1) : 
  if j % sum(map(int,str(j))) == 0 :
    cnt += 1

print(cnt)
"""