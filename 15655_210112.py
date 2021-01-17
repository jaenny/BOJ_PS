from itertools import combinations
n,m=map(int,input().split())
lst=[int(x) for x in input().split()]

lst = list(combinations(lst,m))

res=[]
for i in lst : 
  i=sorted(list(i))
  res.append(i)

res.sort()

for i in res :
  print(*i)