from itertools import combinations

n=int(input())
arr=[[0]*(n+1)]
items=[]
for i in range(n) :
  items.append(i+1)
  arr.append([0]+list(map(int,input().split())))

res=[]
for i in list(combinations(items,n//2)):
  res.append(i)

ans = 999999999999999999999
for i in range(len(res)//2) :
  start = 0
  link = 0
  starttemp=[]
  linktemp=[]

  for j in list(combinations(res[i],2)) :
    starttemp.append(j)

  for t in starttemp :
    start = start + arr[t[0]][t[1]] + arr[t[1]][t[0]]
  for k in list(combinations(res[len(res)-i-1],2)) :
    linktemp.append(k)

  for k in linktemp :
    link = link + arr[k[0]][k[1]] + arr[k[1]][k[0]]
  
  if ans > abs(start-link) :
    ans = abs(start-link)


print(ans)