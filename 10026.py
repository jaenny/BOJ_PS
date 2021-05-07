from collections import deque

#입력
n=int(input())
matrix=[]
for i in range(n):
  newline=list(map(str,input()))
  matrix.append(newline)

#bfs 탐색
def bfs(queue,cnt) :
  direction = [[0,1],[1,0],[-1,0],[0,-1]]
  while queue :
    node = queue.popleft()
    i = node[0]; j = node[1]
    color = matrix[i][j]

    for d in direction :
      di = i + d[0]; dj = j + d[1]
      if 0<=di<n and 0<=dj<n and matrix[di][dj] == color and visit[di][dj]==0 :
        visit[di][dj] = 1
        queue.append([di,dj])
  return cnt + 1

#적록색약이 아닌 경우
#평범한 bfs 탐색
#recurssion error 가 발생할까봐 bfs로 풀었음.
visit=[[0]*n for i in range(n)]
q=deque()
cnt = 0
for i in range(n) :
  for j in range(n) :
    if visit[i][j] == 0 :
      visit[i][j] = 1
      q.append([i,j])
      cnt = bfs(q,cnt)
print(cnt,end=" ")

#적록색약인 경우
#R과 G를 구분하지 못한다 -> matrix에서 R을 G로 모두 바꿔줌.
#bfs 탐색 진행
for i in range(n) :
  for j in range(n) :
    if matrix[i][j] == "R" :
      matrix[i][j] = matrix[i][j].replace("R","G")

visit=[[0]*n for i in range(n)]
q=deque()
cnt = 0
for i in range(n) :
  for j in range(n) :
    if visit[i][j] == 0 :
      visit[i][j] = 1
      q.append([i,j])
      cnt = bfs(q,cnt)
print(cnt)