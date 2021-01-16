n,m=map(int,input().split())
hear=set()
see=set()
for i in range(n) :
  name=input()
  hear.add(name)
for i in range(m) :
  name=input()
  see.add(name)
res = hear&see
res=sorted(res)
print(len(res))
for i in range(len(res)) :
  print(res[i])