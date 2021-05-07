from collections import deque
k = int(input())
w,h = map(int,input().split())

#matrix 만들기
matrix = [list(map(int, input().split())) for i in range(h)]

#visit 만들기
visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]

#원숭이, 말의 움직임
monkey = [[0,1],[1,0],[-1,0],[0,-1]]
horse = [[2,1],[1,2],[-2,1],[-1,2],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs() :
  queue = deque()
  queue.append((0,0,k)) # i idx, j idx, # of horse move left

  while queue :
    i,j,cnt = queue.popleft()

    #종료조건
    if i == h-1 and j == w-1 : return visit[i][j][cnt]    
    
    #monkey move
    for md in monkey : 
      mi = i + md[0]
      mj = j + md[1]
      if 0 <= mi < h and 0 <= mj < w and matrix[mi][mj] == 0 and visit[mi][mj][cnt] == 0 :
        visit[mi][mj][cnt] = visit[i][j][cnt] + 1
        queue.append((mi,mj,cnt))

    #horse move
    if cnt > 0 : #말의 움직임을 사용할 수 있는 횟수가 남아있다면
      for hd in horse :
        hi = i + hd[0]
        hj = j + hd[1]
        if 0 <= hi < h and 0<= hj < w and matrix[hi][hj] == 0 and visit[hi][hj][cnt-1] == 0 :
          visit[hi][hj][cnt-1] = visit[i][j][cnt] + 1
          queue.append((hi,hj,cnt-1))
  return -1

print(bfs())