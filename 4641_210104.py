while(True) :
  cnt = 0
  L=list(map(int,input().split()))
  if -1 in L :
    break
  L.sort()
  for i in range(1,len(L)) :
    if 2*L[i] in L :
      cnt +=1
  print(cnt)