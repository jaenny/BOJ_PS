from math import *
t = int(input())
temp=[]

def div(k,x) :
  while x!=1 :
    if x % k == 0 :
      temp.append(k)
      x/=k
    else : k+=1

for j in range(t) :
  temp=[]
  res=[]
  num = int(input())
  div(2,num)
  tempset = set(temp)
  for i in tempset :
      cnt = temp.count(i)
      if cnt >= 2 :
        if (cnt == (cnt&-cnt)) :
          res.append(int(pow(i,cnt)))
        else :
          chk = 1
          for k in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824] :
            if k > cnt :
              chk = k//2
              break
          res.append(int(pow(i,chk)))
          res.append(int(pow(i,cnt-chk)))
      else :
        res.append(i)
  print(' '.join(str(x) for x in sorted(res)))