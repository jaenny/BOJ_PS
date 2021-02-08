n,m=map(int,input().split())
matrix=[]
for i in range(n) :
  newline=input()
  matrix.append([])
  for j in newline :
    matrix[-1].append(j)

#왼쪽위, 오른쪽 아래 꼭짓점 찾기
c=0
for i in range(n) :
  for j in range(m) :
    if matrix[i][j]=='#' : 
      leftup=[i,j]
      c=1
      break
  if c==1 :break

for i in range(n) :
  for j in range(m) :
    if matrix[n-1-i][m-1-j]=='#' :
      rightdown=[n-1-i,m-1-j]
      break
  break

#나머지 두 꼭짓점 찾기
leftdown=[rightdown[0],leftup[1]]
rightup=[leftup[0],rightdown[1]]

#결과물 출력
flag = 0
for i in range(leftup[1]+1,rightup[1]) :
  if matrix[leftup[0]][i] == '.' : 
    print('UP')
    flag == 1
    break
if flag == 0 :
  for i in range(leftdown[1]+1,rightdown[1]) :
    if matrix[leftdown[0]][i]=='.' :
      print('DOWN')
      flag == 1
      break
if flag == 0 :
  for i in range(leftup[0]+1,leftdown[0]) :
    if matrix[i][leftup[1]]=='.' :
      print('LEFT')
      flag == 1
      break
if flag == 0 :
  for i in range(rightup[0]+1,rightdown[0]) :
    if matrix[i][rightup[1]]=='.' :
      print('RIGHT')
      break