n=int(input())

dp=[0,0,1,1]+[0]*n

for i in range(4,n+1) :
  temp_res=[]
  if i % 3 == 0 :
    temp = i // 3
    temp_res.append(dp[temp] + 1)
  if i % 2 == 0 :
    temp = i // 2
    temp_res.append(dp[temp] + 1)
  if True :
    temp = i - 1
    temp_res.append(dp[temp] + 1)
  dp[i] = min(temp_res)

print(dp[n])