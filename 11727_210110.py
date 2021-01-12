n=int(input())
L=[1,3]

for i in range(2,n) :
  new = 2*L[i-2] + L[i-1]
  L.append(new)
if n == 1 :
  print(1)
else : print(L[-1]%10007)