n=int(input())
arr_x=[-1]*n; arr_y=[-1]*n

def dfs(y,x) :
  #가지치기
  for i in range(y) :
    #y가 같은 위치 = 가로로 겹침
    if y == arr_y[i] : return 0
    #x가 같은 위치 = 세로로 겹침
    if x == arr_x[i] : return 0
    #대각선 겹침
    if (abs(x-arr_x[i]) == abs(y-arr_y[i])) : return 0
  
  #종료조건
  if y == n-1 : 
    return 1
  
  #가지치기를 통과했지만 아직 종료조건이 아니라면
  #퀸을 둔 곳의 위치 저장
  arr_y[y] = y
  arr_x[y] = x
  
  #dfs탐색
  cnt = 0
  for i in range(n) :
    cnt = cnt + dfs(y+1,i)
  return cnt

cnt = 0
for i in range(n) :
  cnt = cnt + dfs(0,i)
print(cnt)