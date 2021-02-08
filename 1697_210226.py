"""
from collections import deque
import sys

#입력
start,end=map(int,sys.stdin.readline().split())

#start와 end만으로 답을 구할 수 있는 경우
if start == end : print(0)
elif abs(start-end) == 1 or start * 2 == end : print(1)
elif start > end : print(start-end)

#그 외 추가적인 연산이 필요한 경우
else :
  queue=deque()
  visit={}

  def cal(root) :
    for i in range(3) :
      if i == 0 : new = root * 2
      elif i == 1 : new = root - 1
      else : new = root + 1

      if 0<= new <= 100000 :
        if new not in visit : 
          visit[new] = visit[root]+1
          queue.append(new)

  visit[start] = 0
  cal(start)

  while queue :
    x = queue[0]
    queue.popleft()
    if x == end : 
      print(visit[x])
      break
    cal(x)
    """



from collections import deque

start,end=map(int,input().split())

#start와 end만 가지고 답을 구할 수 있는 경우
if start == end : print(0)
elif abs(start-end) == 1 or start * 2 == end : print(1)
elif start > end : print(start-end)
#추가적인 연산이 필요한 경우
else :
  queue=deque()
  visit=[0]*100001
  
  visit[start] = 1
  if 0<=start + 1<=100000 :
    queue.append([start+1,1])
  if 0<=start-1<=100000 :
    queue.append([start-1,1])
  if 0<=start*2<=100000 :
    queue.append([start*2,1])
  
  while queue :
    check = queue[0][0]
    second = queue[0][1]
    queue.popleft()
    if visit[check] == 0 :
      visit[check] = 1
      if check == end : 
        print(second)
        break
      else :
        temp=[check+1,check-1,check*2]
        for item in temp :
          if 0<= item <= 100000 :
            queue.append([item,second+1])