from collections import deque

A,B,C =map(int,input().split())

visit = [[[0]*(C+1) for _ in range(B+1)] for _ in range(A+1)]

q = deque()
q.append([0,0,C])

ans=[]

while q :
  node = q.popleft()

  a = node[0]
  b = node[1]
  c = node[2]

  if visit[a][b][c] == 1 : continue
  visit[a][b][c] = 1

  if a == 0 : ans.append(c)

  #A에서 옮기기
  #A -> B
  if (a+b > B) : q.append([a+b-B,B,c])
  else : q.append([0,a+b,c])
  #A -> C
  if (a+c > C) : q.append([a+c-C,b,C])
  else : q.append([0,b,a+c])

  #B에서 옮기기
  #B -> A
  if (b+a > A) : q.append([A,a+b-A,c])
  else : q.append([a+b,0,c])
  #B -> C
  if (b+c > C) : q.append([a,b+c-C,C])
  else : q.append([a,0,b+c])

  #C에서 옮기기
  #C -> A
  if (c+a > A) : q.append([A,b,a+c-A])
  else : q.append([a+c,b,0])
  #C -> B
  if (c+b > B) : q.append([a,B,c+b-B])
  else : q.append([a,c+b,0])

ans = ' '.join(str(x) for x in sorted(ans))
print(ans)