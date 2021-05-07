n,m=map(int,input().split())
ans = 0
arr=list(map(int,input().split()))
res=[]
for i in range(n-2) :
  ans = 0
  ans = ans + arr[i]
  firstans = ans
  for j in range(i+1,n-1) :
    if firstans+arr[j] > m : continue
    else :
      ans = firstans + arr[j]
      beforeans = ans
    for k in range(j+1,n) :
      if beforeans + arr[k] > m : continue
      ans = max(ans, beforeans + arr[k])
      res.append(ans)

print(max(res))
