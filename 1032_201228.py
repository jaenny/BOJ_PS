num = int(input())
files=[]

for i in range(num) :
  files.append(input())

res=[]

for j in range(len(files[0])) :
  bchanged = 0
  for i in range(1,num) :
    org = files[0][j]
    if files[i][j] == org :
      bchanged = 0
    else : 
      bchanged = 1
      break
  if bchanged == 1 :
    res.append('?')
  else :
    res.append(files[i][j])

for i in res :
  print(i,end='')
