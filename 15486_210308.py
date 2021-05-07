days=int(input())
T=[0]*(days+2); P=[0]*(days+2)
for i in range(1,days+1) : 
  t,p=map(int,input().split())
  T[i] = t; P[i] = p
dp=[0]*(days+2)

for i in range(1,days+1) :
  if i+T[i] <= days+1 :
    dp[i+T[i]] = max(dp[i+T[i]],dp[i]+P[i])
  dp[i+1] = max(dp[i],dp[i+1])

print(dp[-1])