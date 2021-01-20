def pi(n) :
  if n==0 : return 0
  elif n== 1 or n== 2 : return 1
  elif n == 3 : return 2
  else : 
    return pi(n-1)+pi(n-2)
n=int(input())
print(pi(n))