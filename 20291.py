n=int(input())
L={}
for i in range(n):
  a,b=input().split('.')
  if b in L :
    L[b] = L[b]+1
  else :
    L[b] = 1
L_s=sorted(L)
for k in L_s :
  print(k,'',end='')
  print(L[k])