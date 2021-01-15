n=int(input())

visit=[]
res=[]
def perm(now,cnt) :
  if cnt == n :
    for i in res : 
      print(i,end=' ')
    print()
    return 
  for i in range(1,n+1) :
    if i not in visit :
      visit.append(i)
      res.append(i)
      perm(i,cnt+1)
      res.pop()
      visit.remove(i)

for i in range(1,n+1) :
  visit.append(i)
  res.append(i)
  perm(i,1)
  res.pop()
  visit.remove(i)

