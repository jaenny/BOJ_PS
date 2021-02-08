n=input()
numbers=[int(x) for x in input().split()]
count = 0
for num in numbers : 
  if num == 1 : continue
  flag = 0
  for i in range(2,num) :
    if num % i == 0 :
      flag = 1
      break
  if flag == 0 : count+=1

print(count)