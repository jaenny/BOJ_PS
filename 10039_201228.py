score=[]
for i in range(5):
  new = int(input())
  if new < 40 :
    new = 40
  score.append(new)

print(int(sum(score)/5))