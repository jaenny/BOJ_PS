direct = [[-1,0],[0,-1],[1,0],[0,1]] #위쪽, 왼쪽, 아래쪽, 오른쪽 순서로 탐색

def bfs(matrix,i,j) :
  while queue :
    i = queue[0][0]
    j = queue[0][1]
    node = queue.pop(0)
    for d in direct :
      di = i + d[0]
      dj = j + d[1]
      if (di >=0 and dj >=0 and di < n and dj <m) and matrix[di][dj] == 1 :
        if di == 0 and dj == 0 : continue #시작 지점을 다시 count하는 경우 제외
        matrix[di][dj] = matrix[i][j] + 1
        queue.append([di,dj])

n,m=map(int,input().split())
matrix=[]

for i in range(n) :
  new = input()
  matrix.append([])
  for x in new :
    matrix[-1].append(int(x))

queue=[[0,0]]
bfs(matrix,0,0)
print(matrix[-1][-1])