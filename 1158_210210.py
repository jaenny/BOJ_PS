#[BOJ] 백준 파이썬 > 1158번 요세푸스 문제 
n, k = map(int,input().split()) 
arr = [int(x) for x in range(1,n+1)]
res=[]

idx = 0

while len(res) != n :
  idx = (idx + (k-1)) % len(arr)
  res.append(arr.pop(idx))
  print(res)