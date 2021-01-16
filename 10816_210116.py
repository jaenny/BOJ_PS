import sys

n=sys.stdin.readline()
check = sorted(map(int,input().split()))
m=sys.stdin.readline()
L=list(map(int,input().split()))
dic={}

for x in check :
  if x in dic :
    dic[x] +=1
  else :
    dic[x] = 1

print(' '.join(str(dic[x]) if x in dic else '0' for x in L))