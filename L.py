from collections import deque
n=int(input())

direct = [[1,0],[0,1],[-1,0],[0,-1]]

matrix=[['.']*(n+2)]
for _ in range(n) :
  new = ['.']+list(map(str,input()))+['.']
  matrix.append(new)
matrix.append(['.']*(n+2))

visit=[[0]*(n+2) for _ in range(n+2)]

for i in range(1,n+1) :
  for j in range(1,n+1) :
    if matrix[i][j] == 'X' :
      for d in direct :
        di = i + d[0]
        dj = j + d[1]
        if matrix[di][dj] == '.' :
          if di == i : #같은 가로 줄에 있다면
            for k in range(1,n+1) :
              if matrix[di][k] == '.' :
                visit[di][k] += 1
              elif k == j : continue
              else : break
          if dj == j :
            for k in range(1,n+1) :
              if matrix[k][dj] == '.' :
                visit[k][dj] += 1
              elif k == i : continue
              else : break
    print(i,j)
    for m in range(1,n+1) :
      print(visit[m][1:-1])
    print('--------')