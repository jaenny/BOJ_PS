n,m=map(int,input().split())

if m > n//2 : m = n - m
div = 1
for i in range(2,m+1) :
  div = div * i
ori = 1
for j in range(m) :
  ori = ori * (n-j)

print(ori//div)