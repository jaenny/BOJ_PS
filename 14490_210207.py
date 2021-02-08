def gcd(a,b) :
  if b == 0 : return a
  else : return gcd(b,a%b)

a,b=input().split(':')
a=int(a);b=int(b)

div=gcd(a,b)

a=int(a/div)
b=int(b/div)

print("%d:%d"%(a,b))