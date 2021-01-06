import sys

num=int(sys.stdin.readline())

L=[0,1]
L_before=[]
cnt = 1
while(num>=2 and cnt!=num) :
  L_before=L.copy()
  L[0] = L_before[1]
  L[1] = L_before[1] + L_before[0]
  cnt += 1

print(L[0],L[1])
