from collections import deque
t=int(input())

queue=deque()
direct = [[0,-1],[0,1],[1,0],[-1,0]] #4방향 탐색

for _ in range(t) :
  m,n,k=map(int,input().split())
  matrix=[[0]*m for _ in range(n)]
  visit=[[0]*m for _ in range(n)]
  for _ in range(k) :
    x,y=map(int,input().split())
    matrix[y][x] = 1

  cnt = 0 #지렁이 마리 수 카운트
  for i in range(n) : 
    for j in range(m) : 
      queue=deque()
      #2차원 배열 matrix를 모두 돌면서
      #아직 방문하지 않았고, 배추가 심어진 곳이라면 bfs 탐색 진행
      if visit[i][j] == 0 and matrix[i][j] == 1 :
        cnt +=1
        visit[i][j] = cnt #방문배열에 지렁이 개수 저장
        queue.append([i,j])
        while queue :
          node = queue.popleft()
          y = node[0]
          x = node[1]
          for d in direct : 
            di = y + d[0]
            dj = x + d[1]
            if 0<=di<n and 0<=dj<m and visit[di][dj] == 0 and matrix[di][dj] == 1 :
              visit[di][dj] = cnt
              queue.append([di,dj])
  print(cnt)
