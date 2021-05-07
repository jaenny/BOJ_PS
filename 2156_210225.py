n=int(input())
arr=[0]
for _ in range(n) :
  arr.append(int(input()))

dp = [[0]*3 for _ in range(n+1)]

pos = 2

for i in range(1,n+1) :
  if i == 1 :
    dp[i] = [arr[i],arr[i],0]
  elif i == 2 :
    dp[i] = [dp[1][0]+arr[i], dp[1][0], arr[i]]
  else :
    new = dp[i-1][pos]
    if pos == 0 :
      dp[i] = [new, dp[i-1][1]+arr[i], dp[i-1][2]+arr[i]]
    elif pos == 1 :
      dp[i] = [dp[i-1][0]+arr[i], new, dp[i-1][2]+arr[i]]
    elif pos == 2 :
      dp[i] = [dp[i-1][0]+arr[i], dp[i-1][1]+arr[i], new]
  print(i,dp[i])
  if pos == 0 : pos = 2
  else : pos -= 1

print(max(dp[n]))