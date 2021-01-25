n=int(input())
arr=[]
for x in range(n) :
  arr.append(int(input()))
dp=[1]*n
maximum = 0
for i in range(n) :
  for j in range(i) :
    if (arr[j] < arr[i] and dp[i] < dp[j]+1) :
      dp[i] = dp[j] + 1
print(n-max(dp))