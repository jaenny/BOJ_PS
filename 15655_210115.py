n,m=map(int,input().split())
lst=[int(x) for x in input().split()]
lst.sort()

visit=[]
res=[]

def per(now,cnt) :
  if cnt == m :
    for i in res :
      print(i, end=' ')
    print()
    return
  for i in range(lst.index(now)+1,len(lst)) :
    if lst[i] not in visit :
      visit.append(lst[i])
      res.append(lst[i])
      per(lst[i],cnt+1)
      res.pop()
      visit.remove(lst[i])

for i in lst :
    visit.append(i)
    res.append(i)
    per(i,1)
    res.pop()
    visit.remove(i)