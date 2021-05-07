from collections import deque
n = int(input())

queue = deque()
ans = [-1]*(n+1) #정답을 저장할 리스트
rumor = [0]*(n+1) #주변에 루머를 믿는 지인이 몇 명인지 저장할 리스트

#지인 입력 받기
ppl = {}
for i in range(1,n+1) :
  newinput = list(map(int,input().split()))
  newinput.pop()
  ppl[i] = newinput

#최초 유포자
m = int(input())
queue = deque(map(int,input().split()))

#최초유포자들을 0분으로 초기화
for i in queue :
  ans[i] = 0

#bfs탐색
while queue :
  x = queue.popleft()
  for item in ppl[x] :
    rumor[item] = rumor[item] + 1 #주변에 루머를 믿는 지인 1명 추가
    if ans[item] == -1 and rumor[item]*2 >= len(ppl[item]) :
      ans[item] = ans[x] + 1
      queue.append(item)

#출력
print(' '.join([str(ans[i]) for i in range(1,len(ans)) ]))
