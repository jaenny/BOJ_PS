import sys
n=int(sys.stdin.readline())
L=[int(x) for x in sys.stdin.readline().split()]
L=list(set(L))
L.sort()
for i in L :
  print(i,end=' ')