n=int(input())
L=[]
i=666
cnt = 0
while(True) :
  j=i
  cnt=0
  if list(map(int,str(j))).count(6) >= 3 :
    for k in str(j) :
      if k == "6" : cnt+=1
      else : cnt = 0
      if cnt == 3 : 
        L.append(i)
        break
  if len(L) == n :
    break
  i+=1

L.sort()
print(L[n-1])
