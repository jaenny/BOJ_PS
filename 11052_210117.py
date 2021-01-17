n=int(input())
maximum=[0]*(n+1)
price=[0]+[int(x) for x in input().split()]
maximum[1]=price[1] #각 카드를 만드는데 드는 최대 비용
for i in range(2,n+1) :
  for j in range(1,i+1) :
    if maximum[i] < maximum[i-j] + price[j] :
      maximum[i] = maximum[i-j] + price[j]

print(maximum[n])