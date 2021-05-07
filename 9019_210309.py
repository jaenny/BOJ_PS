from collections import deque
t=int(input())

for _ in range(t) :
  a,b=input().split()
  a=int(a);b=int(b)
  queue = deque()
  queue.append([a,'']) #입력받은 수 A와 연산들을 저장할 문자
  visit = [0]*10000 #방문 체크 배열

  while queue : 
    node = queue.popleft()
    num = node[0]
    order = node[1]
    
    #종료조건
    if num == b and order!='': #order!=''이 없을 경우 0 0 입력했을 때 아무것도 출력 안됨.
      print(order)
      break

    #D
    newD = num*2
    if newD > 9999 : newD = (num*2) % 10000
    if visit[newD] == 0 :
      visit[newD] = 1
      queue.append([newD,order+'D'])

    #S
    newS = num - 1
    if num == 0 : newS = 9999
    if visit[newS] == 0 :
      visit[newS] = 1
      queue.append([newS,order+'S'])

    #L
    newL = int(num % 1000 * 10 + num / 1000)
    if visit[newL] == 0 :
      visit[newL] = 1
      queue.append([newL,order+'L'])
    
    #R
    newR = int(num % 10 * 1000 + num // 10)
    if visit[newR] == 0 :
      visit[newR] = 1
      queue.append([newR,order+'R'])
