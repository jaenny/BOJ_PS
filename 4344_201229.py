test=int(input())
List=[]
add=[]
sum = 0
cnt = 0
for i in range(test) :
  add=[int(x) for x in input().split()]
  List.append(add)

for i in range(len(List)) :
  sum = 0
  for j in range(1,len(List[i])) :
    sum = sum + List[i][j]
  List[i].append(sum/List[i][0])

for i in range(len(List)) :
  cnt = 0
  for j in range(1,len(List[i])) :
    if List[i][j] > List[i][-1] :
      cnt += 1
  print("%.3f%%" %(cnt/List[i][0]*100))