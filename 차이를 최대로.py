n=int(input())
L=sorted(map(int,input().split()))
print(L)
res=[L[0]]
L.remove(L[0])

for i in range(len(L)) :
  if len(L) == 2 :
    back=L[-1]; front=L[0]
    if abs(res[0]-back) + abs(res[-1]-front) > abs(res[0]-front) + abs(res[-1]-back) :
      res.insert(0,back); res.append(front)
    else : 
      res.insert(0,front); res.append(back)
    L.remove(back); L.remove(front)
  elif len(L)!=0 :
    if i%2 == 0 : #큰 쪽에서 뽑기
      new = L[-1]
      if abs(res[0] - new) > abs(res[-1]-new) :
        res.insert(0,new)
      else :
        res.append(new)
    else : #작은 쪽에서 뽑기
      new = L[0]
      if abs(res[0] - new) > abs(res[-1]-new) :
        res.insert(0,new)
      else :
        res.append(new)
    L.remove(new)
    print(res)
print(res)
ans=0
for j in range(len(res)-1) :
  ans = ans + abs(res[j]-res[j+1])

print(ans)