def fac(n):
  if n > 1 :
    res=n*fac(n-1)
    return res
  else : 
    return 1

cnt=0
num=int(input())
num=fac(num)
while(True) :
  if num % 10 == 0:
    num = num//10
    cnt +=1
  else : break
print(cnt)

"""
틀렸음!!!!
n=int(input())
print(n//5)
"""