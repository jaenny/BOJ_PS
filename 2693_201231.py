n=int(input())
for i in range(n) : 
  L=[int(x) for x in input().split()]
  L.sort(reverse=True)
  print(L[2])