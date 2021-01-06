L=[]
for i in range(9) :
  num=L.append(int(input()))

ans=1

maximum = max(L)
print(maximum)

for l in L : 
  if l == maximum :
    break
  else : 
    ans+=1

print(ans)