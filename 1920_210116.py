import sys

n=int(sys.stdin.readline())
check = sorted(list(map(int,sys.stdin.readline().split())))
m=int(sys.stdin.readline())
L=list(map(int,sys.stdin.readline().split()))

def binarySearch(item,check,start,end) :
  if start > end :
    return 0
  m = (start+end)//2
  if item == check[m] : return 1
  elif item < check[m] : return binarySearch(item, check, start, m-1)
  else : return binarySearch(item, check, m+1, end)

for item in L :
  start = 0
  end = len(check)-1
  print(binarySearch(item,check,start,end))