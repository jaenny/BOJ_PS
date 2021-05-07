n,s,m = map(int,input().split())
volume = [0] + list(map(int,input().split()))
dp = [[0]*(m+1) for i in range(n+2)]
dp[1][s] = 1

for i in range(2,n+2) :
  temp=[]
  for j in range(m+1) :
    if dp[i-1][j] == 0 : continue
    else :
      up = j + volume[i-1]
      if 0 <= up <= m :
        dp[i][up] = 1
        temp.append(up)
      down = j - volume[i-1]
      if 0 <= down <= m :
        dp[i][down] = 1
        temp.append(down)
  if len(temp) == 0 : 
    print(-1)
    break

if len(temp) != 0 : print(max(temp))