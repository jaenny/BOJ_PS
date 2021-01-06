import sys

def fac(n):
  if n>1:
    return n*fac(n-1)
  elif n==1:
    return 1
  elif n==0 :
    return 1

n,k = sys.stdin.readline().split()
n=int(n); k=int(k)
ans = fac(n)/(fac(k)*fac(n-k))
print(int(ans))