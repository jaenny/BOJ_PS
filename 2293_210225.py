n,k=map(int,input().split())
numarr=[0]
for _ in range(n) :
  numarr.append(int(input()))

numarr.sort() #오름차순 정렬

dp=[0]*(k+1)

for i in range(1,n+1) :
  num = numarr[i]
  for j in range(1,k+1) :
    if j == num : 
      dp[j] = dp[j] + 1
    elif j < num :
      dp[j] = dp[j]
    else :
      dp[j] = dp[j] + dp[j-num]

print(dp[k])