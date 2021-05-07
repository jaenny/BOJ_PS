n=int(input())
arr=list(map(str,input().split()))

ans = int(arr[0])
for i in range(1,n*2-1) :
  if arr[i] == '*' :
    n = int(arr[i+1])
    ans = ans*n
  elif arr[i] == '/' :
    n = int(arr[i+1])
    ans = ans/n

if int(ans) == ans : 
  print('mint chocolate')
else :
  print('toothpaste')