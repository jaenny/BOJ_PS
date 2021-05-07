n = int(input())
arr = [0]*n
for i in range(n) :
  arr[i] = float(input())
dp = [0] * n
dp[0] = arr[0]
for i in range(1,n) :
  dp[i] = max(dp[i-1]*arr[i],arr[i])

print("%.3f" %max(dp))