not_selfnum=[]
for i in range(1,10001) :
  check = (i + i//10000 + (i%10000//1000) + (i%10000%1000//100) + (i%10000%1000%100//10) + (i%10000%1000%100%10))
  if check in not_selfnum :
    continue
  else :
    not_selfnum.append(check)

for j in range(1,10001) :
  if j not in not_selfnum :
    print(j)
