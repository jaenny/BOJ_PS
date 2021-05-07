n,m=map(int,input().split())

matrix=[[0]*m for _ in range(n)] #그래프 생성

matrix[0][0] = 1 #원래는 1이지만 dp 계산을 위해 1로 바꿈

for i in range(n) :
  for j in range(m) :
    # 오른쪽
    if j+1 < m : #밖으로 안 벗어 난다면
      matrix[i][j+1] = matrix[i][j+1] + matrix[i][j]
    
    # 아래
    if i+1 < n : #밖으로 안 벗어 난다면
      matrix[i+1][j] = matrix[i+1][j] + matrix[i][j]
    
    #대각선
    if i+1 < n and j+1 < m : #밖으로 안 벗어 난다면
      matrix[i+1][j+1] = matrix[i+1][j+1] + matrix[i][j]

print(matrix[-1][-1]%1000000007)