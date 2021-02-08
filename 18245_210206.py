count = 1
while True :
  s=input()
  if s == 'Was it a cat I saw?' : break
  a=s[::count+1]
  print(a)
  count +=1