n,m=map(int,input().split())
nope={}
for i in range(n) :
  nope[i+1]=[]

for _ in range(m) :
  a,b=map(int,input().split())
  if a not in nope[b] : nope[b].append(a)
  if b not in nope[a] : nope[a].append(b)

print(nope)
visit=[]
count = 0

def dfs(now,depth) :
  global count
  if depth == 3 :
    count+=1
    print(visit)
    return

  for i in range(now+1,n+1) :
    visit.append(i)
    #if i not in nope[now] :
    if len(list(set(visit)&set(nope[i]))) == 0 :
      dfs(i,depth+1)
    visit.remove(i)

for i in range(1,n+1) :
  visit.append(i)
  dfs(i,1)
  visit.remove(i)

print(count)

