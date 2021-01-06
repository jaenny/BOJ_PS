import sys

def labelDFS(v, color) :
  visit[v] = 1
  label[v] = color
  for i in range(n) :
    if adj[v][i] != 0 and visit[i] == 0 :
      labelDFS(i,color)

n,m = map(int,sys.stdin.readline().split())
count = 0

adj=[]
for i in range(n) : #인접 배열 초기화
  adj.append([])
  for j in range(n) :
    adj[i].append(0)

for i in range(m) :
  a,b = map(int,sys.stdin.readline().split())
  adj[a-1][b-1] = adj[b-1][a-1] = 1 #무방향 그래프

visit=[]
label=[]
for i in range(n) :
  visit.append(0) #방문 체크 배열 초기화
  label.append(0) #연결 요소 체크 배열 초기화


for i in range(n) :
  if visit[i] == 0 :
    count += 1
    labelDFS(i,count)

print(count);