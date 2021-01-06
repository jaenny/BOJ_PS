test = int(input())

for i in range(test) :
  num,word = input().split()
  num = int(num)
  for j in word :
    print(j*num ,end='')
  print('')