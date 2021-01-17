n=int(input())
visit=[]
def perm(now,cnt) :
  if cnt == n :
    for i in visit : 
      print(i,end=' ')
    print()
    return 
  for i in range(1,n+1) :
    if i not in visit :
      visit.append(i)
      perm(i,cnt+1)
      visit.pop()
for x in range(1,n+1) :
  visit.append(x)
  perm(x,1)
  visit.pop()

