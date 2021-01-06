n=int(input())
L=[]
for i in range(n) :
  L.append(int(input()))
L.sort()
for j in range(n) :
  print(L[j])