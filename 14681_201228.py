x=int(input()); y=int(input())
res = 0
if x > 0 :
  if y > 0 :
    res = 1
  elif y < 0:
    res = 4
elif x < 0 :
  if y > 0 :
    res = 2
  elif y < 0:
    res = 3
print(res)