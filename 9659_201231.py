"""
n=int(input())
i=0
while(True) :
  if n-3 >= 3 :
    n=n-3
  else :
    n=n-1
  i+=1
  if n == 0 :break


if i % 2 == 0 :
  print("CY")
else : 
  print("SK")
"""
i=int(input())
if i % 2 == 0 :
  print("CY")
else : 
  print("SK")