city=int(input())
matrix=[[0]*city for _ in range(city)]
visit=[]
res = 0
minimum = 10000001

def combination(now, depth) :
  global res,minimum
  flag = 0
  if depth == (city - 1) :
    for i in range(len(visit)) :
      if i == 0 :
        if matrix[0][visit[0]] == 0 : return
        res = matrix[0][visit[0]]
      if i == len(visit)-1 :
        if matrix[visit[-1]][0] == 0 : return
        res = res + matrix[visit[-1]][0]
        break
      if matrix[visit[i]][visit[i+1]] == 0 : return
      res = res + matrix[visit[i]][visit[i+1]]
    if flag == 0 and minimum > res :
      minimum = res

  for j in range(1,city) :
    if j not in visit :
      visit.append(j)
      combination(j,depth+1)
      visit.pop()


#2차원 배열 입력받기
for i in range(city) :
  new=input().split()
  for j in range(city) :
    matrix[i][j] = int(new[j])

#조합 순회
for i in range(1,city) :
  visit.append(i)
  combination(i,1)
  visit.pop()

print(minimum)

