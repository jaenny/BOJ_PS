t=int(input())

L=[1,2,4]

for i in range(3,11) :
  new = L[i-3] + L[i-2] + L[i-1]
  L.append(new)

for i in range(t) :
  n = int(input())
  print(L[n-1])