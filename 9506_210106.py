while(True) :
  n=int(input())
  if n == -1 : break
  L=[]
  sum = 0
  for i in range(1,n):
    if n % i == 0 :
      L.append(i)
      sum = sum + i
  
  if sum == n :
    print(n,'= 1 ',end='')
    for i in range(1,len(L)) :
      print('+ %d '%L[i],end='')
    print('')
  else :
    print(n,'is NOT perfect.')