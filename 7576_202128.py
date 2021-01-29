from collections import deque

x,y=map(int,input().split())
matrix=[[0]*x for _ in range(y)]
visit=[[0]*x for _ in range(y)]
direct = [[0,1],[1,0],[-1,0],[0,-1]]
queue = deque()

#matrix 만들기
for i in range(y) :
  new=input().split()
  for j in range(x) :
    matrix[i][j] = visit[i][j] = int(new[j])
    if matrix[i][j] == 1 :
      queue.append([i,j])

cnt=0

#bfs 탐험
if len(queue) != 0 :
  while queue :
    i = queue[0][0]
    j = queue[0][1]
    queue.popleft()
    for d in direct :
      di = i + d[0]
      dj = j + d[1]
      if (0<=di<y and 0<=dj<x) and matrix[di][dj]==0:
        visit[di][dj] = visit[i][j] + 1
        matrix[di][dj] = 1 #다시 탐색하지 않기 위해 1로 바꿔줌.
        queue.append([di,dj])
        cnt = visit[di][dj] #제일 마지막에 넣는 카운트를 출력하기 위한 변수

#토마토가 있지만 방문 할 수 없는 곳이 있는지, 다 방문했다면 얼마나 걸리는지 출력하는 부분
flag=0
for i in range(y) :
  for j in range(x) :
    if visit[i][j] == 0 : #bfs를 돌고도 방문하지 않은 부분 = 갈 수 없는 부분 = 모든 토마토를 익힐 수는 없다.
      flag = 1
      break
  if flag == 1 : break

if flag == 1 : print(-1)
elif cnt == 0 : print(cnt)
else : print(cnt-1)