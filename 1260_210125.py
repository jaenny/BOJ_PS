node,vertex,root=input().split()
node=int(node); vertex=int(vertex); root=int(root)

def dfs(graph,root) :
  stack=[root]
  while stack :
    node = stack.pop()
    if node not in visit :
      visit.append(node)
      stack.extend(reversed(sorted((graph[node]))))
  return visit

def bfs(graph,root) :
  queue=[root]
  while queue :
    node = queue.pop(0)
    if node not in visit :
      visit.append(node)
      queue.extend(sorted(graph[node]))
  return visit

#그래프 만들기
graph={}
for i in range(vertex) :
  a,b = input().split()
  a=int(a); b=int(b)
  if a not in graph : graph[a] = [b]
  if b not in graph : graph[b] = [a]
  if a not in graph[b] : graph[b].append(a)
  if b not in graph[a] : graph[a].append(b)

if root not in graph :
  graph[root] = [root]

visit=[]
dfs(graph,root)
for item in visit : 
  print(item,end=' ')
print()

visit=[]
bfs(graph,root)

for item in visit : 
  print(item,end=' ')