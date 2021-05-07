n,m = map(int,input().split())
w = [0]+list(map(int,input().split()))
w.sort()
dp = [[-1]*(n+1) for _ in range(m+1)]

for i in range(1,m+1) :
  for j in range(1,n+1) :
    if w[i] == j :
      dp[i][j] = 1
      mul = 2
      while (j * mul) <= n+1 :
        dp[i][j*mul] = mul
        mul += 1

    elif w[i] > j :
      dp[i][j] = dp[i-1][j]
    elif w[i] < j :
      if dp[i][j-w[i]] == 1 :
        dp[i][j] = 1
        mul = 2
        while (j * mul) <= n+1 :
          dp[i][j*mul] = min(dp[i][j*mul],mul)
          mul += 1
      else :
        dp[i][j] = 

for i in range(1,m+1) :
  print(dp[i])