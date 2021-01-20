n,m=map(int,input().split())
L=sorted([int(x) for x in input().split()])
"""
visit=[]
res=[]
printres=[]
def per(now,cnt) :
  if cnt == m :
    s=''
    for i in visit :
      s = s+' '+str(i)
    if s[1:] not in printres :
      printres.append(s[1:])
    return
  
  for i in range(now+1,len(L)) :
    visit.append(L[i])
    per(i,cnt+1)
    visit.remove(L[i])

for i in range(len(L)) :
  visit.append(L[i])
  per(i,1)
  visit.remove(L[i])

for item in printres :
  print(item)
"""
visit=[]
res=[]
printres=[]
def per(now,cnt) :
  if cnt == m :
    for i in visit :
      print(i,end=' ')
    print()
    return
  overlap = 0
  for i in range(now+1,len(L)) :
    if overlap != L[i] :
      visit.append(L[i])
      overlap = L[i]
      per(i,cnt+1)
      visit.remove(L[i])

overlap=0
for i in range(len(L)) :
  if overlap != L[i] :
    visit.append(L[i])
    overlap = L[i]
    per(i,1)
    visit.remove(L[i])
