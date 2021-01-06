import sys

n=int(input())
player={}

for i in range(n) :
  new = sys.stdin.readline()
  if new[0] in player :
    player[new[0]] += 1
  else :
    player[new[0]] = 1

choice=[]

for j in player.keys() :
  if player[j] >=5 :
    choice.append(j)

if len(choice) == 0 :
  print('PREDAJA')
else :
  choice.sort()
  for k in choice :
    print(k,end='')