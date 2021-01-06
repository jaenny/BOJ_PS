n=int(input())
L=[]
M=[int(x) for x in input().split()]
for i in range(n) :
  L.append([])
  L[i].append(M[i])
  L[i].append(i)

L.sort()
sum = 0
for i in range(len(L)) :
  for j in range(i+1) :
    sum = sum + L[j][0]
print(sum)