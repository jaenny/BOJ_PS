n=int(input())
cnt = 0

while n>=3 :
  if n % 5 == 0 : break
  cnt+=1
  n=n-3

if cnt == 0 and n < 3 : #1과 2
  print(-1)
elif n%5 != 0 : #4와 7
  print(-1)
else : 
  print(n//5+cnt)