num = int(input())
ans = num
cnt = 0

while(True) :
  num = (num%10)*10 + (num//10+num%10)%10
  cnt+=1
  if ans == num :
    break
print(cnt)