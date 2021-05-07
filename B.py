n=int(input())
arr=list(map(int,input().split()))
if n == 1 : print(0)
else : 
  chk=[0]*(500001)
  for i in arr :
    chk[i]+=1
  print(max(chk))