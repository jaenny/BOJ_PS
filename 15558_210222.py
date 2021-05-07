from collections import deque
n,k = map(int,input().split())

matrix=[]
visit=[]
for i in range(2) :
  matrix.append([0]+list(map(str,input()))+['1']*k)
  visit.append([0]*(n+1))

queue = deque()
queue.append([1,0,1])#초,라인,층

flag = 0
cnt = 1 #이동하기까지 걸린 시간

while queue :
  node = queue.popleft()
  cnt = node[0]
  line = node[1]
  floor = node[2]

  #종료조건 : n이상 이동할 때
  if floor > n : 
    flag = 1
    print(1)
    break

  if visit[line][floor] == 1 : continue
  visit[line][floor] = 1

  #앞으로 이동
  if matrix[line][floor+1] == '1' :
    queue.append([cnt+1,line,floor+1])
  #뒤로 이동
  if matrix[line][floor-1] == '1' :
    queue.append([cnt+1,line,floor-1])
  #옆 줄로 이동
  if line == 0 :
    if floor+k > n or matrix[line+1][floor+k] == '1':
      queue.append([cnt+1,line+1,floor+k])
  else :
    if floor+k > n or matrix[line-1][floor+k] == '1':
      queue.append([cnt+1,line-1,floor+k])

  #1초에 한 층씩 삭제
  matrix[0][cnt] = '0'
  matrix[1][cnt] = '0'

if flag == 0 : print(0)