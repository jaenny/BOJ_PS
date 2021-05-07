from collections import deque

n,m,k=map(int,input().split())

matrix=[[0]*2 for _ in range(n+1)]

for i in range(1,n+1) :
  l,r = map(int,input().split())
  matrix[i][0] = l
  matrix[i][1] = r

sequence = deque(map(str,input().split()))

res=[0]*(n+1)

for i in range(1,n+1) :
  port = i
  for j in range(len(sequence)) :
    direction = sequence[j]
    if direction == 'L' :
      port = matrix[port][0]
    elif direction == 'R' :
      port = matrix[port][1]
  res[i] = port
  # print(i,res)

start = 1
for i in range(1,k+1) :
  start = res[start]
print(start)