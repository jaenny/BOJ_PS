n=int(input())
L=[]
for i in range(n) :
  a=int(input())
  L.append(a)

l_cnt=1; r_cnt=1
l=L[0]; r=L[n-1]

for i in range(n) : 
  if L[i] > l :
    l=L[i] 
    l_cnt+=1
  if L[n-1-i] > r :
    r=L[n-1-i]
    r_cnt+=1

print(l_cnt); print(r_cnt)