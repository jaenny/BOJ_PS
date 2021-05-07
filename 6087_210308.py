from collections import deque

m,n=map(int,input().split())
matrix = [list(input().strip()) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
ex, ey = -1, 0
queue=deque()



for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'C':
            if ex == -1:
                ex, ey = i, j
            else:
                queue.append((i, j))


direct = [[1,0],[0,1],[-1,0],[0,-1]]

while queue : 
  node = queue.popleft()
  i = node[0]
  j = node[1]

  for d in direct : 
    di = i + d[0]
    dj = j + d[1]
    while 0<=di<n and 0<=dj<m and matrix[di][dj]!='*' :
      if not visit[di][dj] :
        visit[di][dj] = visit[i][j]+1
        queue.append([di,dj])
      di,dj = di+d[0], dj+d[1]

print(visit[ex][ey]-1)