n=int(input())
minimum=[10001]*(n+1)
price=[0]+[int(x) for x in input().split()]
minimum[0]=0
minimum[1]=price[1]
for i in range(2,n+1) :
  L=[]
  for j in range(1,i+1) :
    L.append(minimum[i-j] + price[j])
  minimum[i] = min(L)
print(minimum[-1])