from itertools import combinations

a=[]
n,m=input().split()
n=int(n); m=int(m)

for i in range(n) :
  a.append(i+1)

res=[]
for j in list(combinations(a,m)) :
  res.append(list(j))

for i in range(len(res)) :
  for j in range(len(res[i])) :
    if j == len(res[i]) - 1 : print(res[i][j])
    else : print(res[i][j], end=' ')