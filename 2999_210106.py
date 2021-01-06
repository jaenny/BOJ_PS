import sys
s=sys.stdin.readline()
n=len(s)-1
L=[]
for i in range(1,n) :
  if n % i == 0 :
    if i <= n// i :
      L.append((i,n//i))

msg=[]
k=0
for i in range(L[-1][1]) :
  msg.append([])
  for j in range(L[-1][0]) :
    msg[i].append(s[k])
    k+=1

print(msg)
for i in range(len(msg[i])) :
  for j in range(len(msg)) :
    print(msg[j][i],end='')