h,m,s=(input().split())
h=int(h);m=int(m);s=int(s)
t=int(input())
if t >3600 :
  h=h+t//3600
  m=m+(t%3600)//60
  s=s+((t%3600)%60)
elif t>60 :
  m=m+t//60
  s=s+t%60
else :
  s=s+t

if s>=60:
  s=s-60
  m=m+1
if m>=60:
  m=m-60
  h=h+1
while(h>=24) :
  h=h-24

print(h,m,s)