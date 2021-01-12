def DFS(graph,root) :
    stack = [root]

    while stack :
        node = stack.pop()
        if node not in visit : 
            visit.append(node)
            stack.extend(reversed(graph[node])) #전위순회
    return visit

graph = {}
visit=[]

node,vertex = input().split()
node=int(node); vertex=int(vertex)

for i in range(node) :
  graph[i+1] = []
for i in range(vertex) :
  u, v = input().split()
  u=int(u); v=int(v)
  if v not in graph[u] : graph[u].append(v)
  if u not in graph[v] : graph[v].append(u)

color = 0

for item in graph.keys() :
  if item not in visit :
    color += 1
    DFS(graph,item)

print(color)