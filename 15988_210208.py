mod=1000000009
t=int(input())
n_list=[]

for i in range(t) :
  n_list.append(int(input()))

dp=[0]*(max(n_list)+1)
dp[1] = 1; dp[2] = 2; dp[3] = 4

for i in range(4,max(n_list)+1) :
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod

for num in n_list :
  print(dp[num])
