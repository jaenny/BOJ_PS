days=int(input())
T=[0]*days; P=[0]*days
for i in range(days) : 
  t,p=map(int,input().split())
  T[i] = t; P[i] = p
dp=[0]*days

for i in range(days) :
  res=[]
  if i + T[i] <= days :
    dp[i] = P[i]
    for j in range(i) :
      if T[j] + j < i+1 : #날짜가 안넘으면서
        if dp[i] + dp[j] > dp[i] :
          res.append(dp[i] + dp[j])
  if len(res) != 0 : dp[i] = max(res)

print(max(dp))