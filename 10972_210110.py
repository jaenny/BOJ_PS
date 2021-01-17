from itertools import permutations

num=[int(x)+1 for x in range(int(input()))]
check = [int(x) for x in input().split()]
per=[]

cnt = 0
for i in permutations(num,len(num)) :
  per.append(list(i))
  if cnt == 1 : break
  if list(i) == check :
    cnt = cnt + 1

c = per[-1].copy()
c.sort(reverse=True) 

if per[-1] == c : print(-1)
else : 
  for i in per[-1] :
    print(i, end=' ')