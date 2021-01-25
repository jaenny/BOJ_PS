n=int(input())
direct=[[0,-1],[-1,0],[0,1],[1,0]] #왼,위,오,아래

def traverse(matrix,i,j,count) :
  if matrix[i][j] == 0 : return count
  matrix[i][j] = 0
  count += 1
  for d in direct : 
    di = i + d[0]
    dj = j + d[1]
    if di < 0 or di >= n or dj < 0 or dj >= len(matrix[0]) :
      continue
    if matrix[di][dj] == 1 :
      count = traverse(matrix,di,dj,count)
  return count
#단지 입력받기
matrix=[]
for i in range(n) :
  new = input()
  matrix.append([])
  for j in new :
    matrix[-1].append(int(j))
    
res=[]
for i in range(n) :
  for j in range(len(matrix[0])) :
    if matrix[i][j] == 1 :
      count = 0
      count = count + traverse(matrix,i,j,count)
      res.append(count)
print(res)