from collections import deque
a,b=map(int,input().split())

queue=deque()
queue.append([a,0])

while queue :
  node = queue.popleft()
  num = node[0]
  count = node[1]
  temp = [num*2,num*10+1]
  flag = 0
  for n in temp :
    if n == b : 
      flag = 1
      print(count+2)
      break
    elif n <b : queue.append([n,count+1])

  if flag == 1 : break

if flag==0 and len(queue)==0 : print(-1)
