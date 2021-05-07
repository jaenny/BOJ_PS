n,m=map(int,input().split())
matrix=[]

for _ in range(n) :
  matrix.append(list(map(int,input().split())))

dp=[[0]*m for _ in range(n)]


for i in range(n) :
  for j in range(m) :
    if i == 0 and j == 0 : dp[0][0] = matrix[0][0]
    elif i == 0 :
      dp[i][j] = dp[i][j-1] + matrix[i][j]
    elif j == 0 :
      dp[i][j] = dp[i-1][j] + matrix[i][j]
    else : 
      dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + matrix[i][j]

print(dp[n-1][m-1])