node = int(input())
edge = int(input())
visit=[]
"""
def dfs(root):
  stack=[root]
  while stack :
    node = stack.pop()
    if node not in visit : 
      visit.append(node)
      stack.extend(graph[node])
"""
def bfs(root) :
  queue=[root]
  while queue :
    n = queue.pop(0)
    if n not in visit :
      visit.append(n)
      queue.extend(graph[n])

graph={}
for _ in range(edge) :
  a,b = map(int,input().split())
  if a not in graph : graph[a]=[b]
  if b not in graph : graph[b]=[a]
  if a not in graph[b] : graph[b].append(a)
  if b not in graph[a] : graph[a].append(b)

if 1 in graph :
  #dfs(1)
  bfs(1)
  print(len(visit)-1)
else :
  print(0)