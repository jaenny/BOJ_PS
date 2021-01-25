n=int(input())
arr=list(map(int,input().split()))
dp=arr.copy()
maximum = 0
for i in range(n) :
  dp[i] = arr[i]
  for j in range(i) :
    if (arr[j] < arr[i] and dp[i] < (dp[j] + arr[i])) :
      dp[i] = dp[j] + arr[i]
      print(i,j,dp[i],arr[i])
  if (maximum < dp[i]) : 
    maximum = dp[i]
print(maximum)