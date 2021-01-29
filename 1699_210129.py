from math import *
n=int(input())
check = [1]
if int(sqrt(n)) == sqrt(n) :
  print(1)
else :
  dp = [int(x) for x in range(n+1)]
  for i in range(2,n+1) :
    if int(sqrt(i)) == sqrt(i) :
      dp[i] = 1
      check.append(i)
    else :
      for j in range(len(check)) :
        new = i - check[len(check)-1-j]
        if dp[i] > 1 + dp[new] :
          dp[i] = 1 + dp[new]
        if dp[i] == 2 : break
  print(dp[n])