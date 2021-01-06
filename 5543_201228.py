burger=[]
drink=[]
for i in range(3) :
  burger.append(int(input()))
for j in range(2) :
  drink.append(int(input()))

res=[]
for i in range(3) :
  for j in range(2) :
    res.append(burger[i]+drink[j])

print(min(res)-50)