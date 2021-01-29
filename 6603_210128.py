res=[]
visit=[]
def com(now,cnt) :
  if cnt == 6 :
    for j in visit :
      print(j,end=' ')
    print()
    return
  
  for i in range(now,len(s)) :
    if s[i] not in visit :
      visit.append(s[i])
      com(i+1,cnt+1)
      visit.remove(s[i])


while True :
  num=list(map(int,input().split()))
  if num == [0] : break
  k=num[0]
  s=num[1:]
  com(0,0)
  print()