def find(n) : 
  cnt = 0
  for div in [64,32,16,8,4,2,1] :
    if n // div == 1 :
      if n % div == 0 :
        cnt += 1
        return cnt
      else : 
        cnt += 1
        n= n % div
        continue
    else : 
      continue
    
num=int(input())
print(find(num))





"""
n=num
cnt = 0
res = 0
if n//64 == 1 :
  res = 1
else :
  if n // 64 >0 : cnt +=1
  n = n%64 
  if n%32 == 0  :
    if n // 32 == 1 : cnt +=1
  else :
    if n // 32 >0 : cnt += 1
    n=n%32
    if n%16 == 0 :
      if n // 16 == 1 : cnt +=1
    else :
      if n // 16 >0 : cnt += 1
      n=n%16
      if n%8 == 0 :
        if n // 8 == 1 : cnt +=1
      else :
        if n // 8 >0 : cnt += 1
        n=n%8
        if n% 4 == 0 :
          if n // 4 == 1 : cnt +=1
        else :
          if n // 4 >0 : cnt += 1
          n=n%4 
          if n == 3 :
            cnt += 2
          elif n == 2 or n == 1 :
            cnt += 1

if num in [1,2,4,8,16,32,64] : print(1)
else : print(cnt)
"""