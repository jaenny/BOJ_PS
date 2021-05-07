dp = [[0]*(1001) for i in range(1001)]

for i in range(1001) :
  for j in range(i,1001) :
    if i==0 : dp[i][j] = 1
    else :
      dp[i][j] = dp[i][j-1] + dp[i-1][j]

while(True) :
  num = int(input())
  if num == 0 : break
  print(dp[num][num])