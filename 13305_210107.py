import sys

city = int(input())
far = [int(x) for x in sys.stdin.readline().split()]
oil = [int(x) for x in sys.stdin.readline().split()]
choice=[]
min = oil[0]

for i in range(len(far)) :
  for j in range(i+1) :
    if min > oil[j] :
      min = oil[j]
  choice.append([far[i],min])

min_cost = 0
for i in range(len(choice)) :
  min_cost = min_cost + choice[i][0]*choice[i][1]

print(min_cost)