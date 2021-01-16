import sys
direct = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
sys.setrecursionlimit(10**6)
def traverse(matrix, i, j) :
  if matrix[i][j] == 0 : return
  matrix[i][j] = 0 #바다로 바꿔줌
  for d in direct :
    my = i + d[0]
    mx = j + d[1]
    if mx <0 or my <0 or mx >= x or my >=y : #지도 밖인지 확인
      continue
    if matrix[my][mx] == 1 : #연결된 섬일 경우 다시 순회
      traverse(matrix, my, mx)

while True :
  x,y=map(int,input().split())
  if x==0 and y==0 : break

  #지도(=matrix) 입력받기
  matrix=[]
  for i in range(y) :
    new = list(map(int,input().split()))
    matrix.append(new)

  #섬의 개수 세기
  count = 0
  for i in range(y) :
    for j in range(x) :
      if matrix[i][j] == 1 : #섬이라면
        count += 1
        traverse(matrix, i , j) #섬과 연결된 다른 섬 찾기
  print(count)