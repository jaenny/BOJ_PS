num=int(input())
scores = [int(x) for x in input().split()]

high = max(scores)

for i in range(len(scores)):
  scores[i] = scores[i]/high*100

print(sum(scores)/num)