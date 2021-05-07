"""
t=int(input())

for i in range(t) :
  new = list(map(int,input().split()))
  m=new[0]; n=new[1]; x=new[2]; y=new[3]

  if x == y : print(x)
  else :
    b = 0
    while True :
      a = (n*b + (y-x))/m
      if n == 1 or m == 1 :
        if n == 1 : print(x)
        else : print(y)
        break
      if b == 99999 : 
        print(-1)
        break
      if a == int(a) : 
        print(int(x+m*a))
        break
      b+=1
"""
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    ans = -1
    for i in range(x, M * N + 1, M):
        print(i)
        if i % N == y:
            ans = i + 1
            
            break
    print(ans)