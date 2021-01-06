n=int(input())

for i in range(n) :
  s = input()
  L=s.split()
  for j in range(len(L)) :
    for k in range(len(L[j])) :
      print(L[j][len(L[j])-1-k],end='')
    print(' ',end='')
  print('')