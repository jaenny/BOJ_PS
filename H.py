n=int(input())
arr=[]


for _ in range(n) :
  l = list(map(int,input().split()))
  arr.append(l)

cnt=0
for i in range(n) :
  for j in range(i+1,n) :
    a1=arr[i][0]
    b1=arr[i][1]
    a2=arr[j][0]
    b2=arr[j][1]
    if a1*b2 != b1*a2 : cnt+=1
print(cnt)
