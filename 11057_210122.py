import sys
n=int(sys.stdin.readline())
L=[[1,1,1,1,1,1,1,1,1,1]]
for i in range(1,n) :
  L.append([])
  for j in range(10) :
    new = 0
    for k in range(j,10) :
      new = new + L[i-1][k]
    L[-1].append(new)
print(sum(L[-1])%1007)






"""
L=[[1,1,1,1,1,1,1,1,1,1]]
for i in range(1,n) :
  L.append([])
  for j in range(10) :
    if j == 0 : 
      L[-1].append(1)
    else : 
      new = L[i][j-1] + L[i-1][j]
      L[-1].append(new)
print(sum(L[-1])%10007)
"""





"""
L=[10,45]
D={1:9,2:8,3:7,4:6,5:5,6:4,7:3,8:2,9:1}
if n != 1 :
  cnt = 2
  while cnt < n :
    r = 0
    before=0
    for i in range(1,10) :
      if i == 1 :
        r = r + sum(D.values())
        before = D[1]
        D[1] = r
      else :
        r = r + D[i-1] - before
        temp = before
        before = D[i]
        D[i] = D[i-1] - temp
    cnt+=1
    L.append(r)

if n == 1 : print(10)
else : print(sum(L)%10007)
"""