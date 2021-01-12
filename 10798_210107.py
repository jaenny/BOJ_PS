L=[[],[],[],[],[]]

for i in range(5) :
  M=list(map(str,input()))
  while(len(M)!=15) :
    M.append(-1)
  L[i].extend(M)

for i in range(15) :
  for j in range(5) :
    if L[j][i] != -1 :
      print(L[j][i],end='')