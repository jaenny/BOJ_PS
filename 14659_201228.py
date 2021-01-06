#시간초과
"""
n=int(input())
L=[int(x) for x in input().split()]
C=[]
for i in range(n) : 
  C[len(C):len(C)]=[0]

for i in range(n) : 
  s=i+1
  for k in range(n-i-1) :
    if L[i] > L[s] :
      s+=1
      C[i]+=1
    else : 
      s+=1
      break

print(max(C))
"""

num=int(input())
hills=[int(x) for x in input().split()]

res=0
highest=0
cnt=0

for hill in hills :
  if hill > highest :
    highest = hill
    cnt = 0
  else : 
    cnt +=1
  res = max(res, cnt)

print(res)