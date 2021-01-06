n=int(input())
L=[]
L_len=[]

for x in range(n):
  w=input()
  L.append(w)
  L_len.append(len(w))
L=list(set(L))
L_len=sorted(list(set(L_len)))

L_res=[]
res=[]
for x in range(len(L_len)) :
  res=[]
  for i in range(len(L)) : 
    if L_len[x] == len(L[i]) : 
      res.append(L[i])
  res=sorted(res)
  L_res.append(res)

k=0
for i in L_res :
  for x in range(len(i)):
    print(L_res[k][x])
  k+=1