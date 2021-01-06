L=[int(x) for x in input().split()]
L_check=[]

for i in range(len(L)) :
  L_check.append(L[i])

L_check.sort()
bchanged = 0

for i in range(len(L)) :
  if L[i] != L_check[i] :
    bchanged = 1
    break

if bchanged == 0 : print("ascending")
elif bchanged == 1 :
  L_check.sort(reverse=True)
  for i in range(len(L)) :
    if L[i] != L_check[i] :
      bchanged = 2
      break
  
  if bchanged == 1 : print("descending")
  else : print("mixed")