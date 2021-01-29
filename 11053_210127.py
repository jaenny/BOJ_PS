n=int(input())

num = list((map(int,input().split())))
dp = [1]*n 

for i in range(len(num)) :
  for j in range(i) :
    if num[i] > num[j] :
      if dp[j] + 1 > dp[i] :
        dp[i] = dp[j] + 1
print(max(dp))

