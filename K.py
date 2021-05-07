from math import *
n=int(input())
divisors = []
def get_divisor(num):
    global divisors
    length = int(sqrt(num)) + 1
    for i in range(1, length):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num//i)
    divisors.sort()
    return divisors

primes=set()

def prime(n) :
  global primes
  a = [False,False] + [True]*(n-1)
  for i in range(2,n+1):
    if a[i]:
      primes.add(i)
      for j in range(2*i, n+1, i):
          a[j] = False

divisors = get_divisor(n)
prime(n)

if len(divisors) == 2 : 
  print(-1)
else : 
  for i in range(1,len(divisors)) :
    if divisors[i] in primes :
      divisors[i] = -1
      divisors[len(divisors)-1-i] = -1
    elif divisors[i] == -1 :
      print(-1)
      break
    else : 
      print(divisors[i],divisors[len(divisors)-1-i])
      break