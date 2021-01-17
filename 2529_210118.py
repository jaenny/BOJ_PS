""" 메모리초과
from itertools import permutations
k=int(input())
check=[x for x in input().split()]
num=[0,1,2,3,4,5,6,7,8,9]
res=[]
for item in permutations(num,k+1) :
  item=list(item)
  for i in range(k) :
    if check[i] == '<' :
      if item[i] > item[i+1] :
        break
    elif check[i] == '>' :
      if item[i] < item[i+1] :
        break
  res.append(item)
for i in max(res) :
  print(i,end='')
print()
for i in min(res) :
  print(i,end='')
"""

k=int(input())
check=[x for x in input().split()]
num=[9,8,7,6,5,4,3,2,1,0]
visit=[]
res=[]
flag=0
def dfs(now,cnt) :
  global flag
  if cnt == k+1 :
    flag = 1
    for i in visit :
      print(i,end='')
    print()
    return

  for i in num :
    if i not in visit and flag == 0:
      visit.append(i)
      if check[cnt-1] == '<' :
        if i > visit[-2] :
          dfs(i,cnt+1)
      else :
        if i < visit[-2] :
          dfs(i,cnt+1)
      visit.remove(i)

for i in num :
  visit.append(i)
  dfs(i,1)
  visit.remove(i)
flag=0
num.reverse()
for i in num :
  visit.append(i)
  dfs(i,1)
  visit.remove(i)