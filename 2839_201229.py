num=int(input())
cnt = 0
count_list=[]
#5만
if num%5==0 :
  count_list.append(num//5)
#3만
if num % 3 == 0 :
  count_list.append(num // 3)
#섞어
while(num >= 3) :
    num = num - 5
    if num % 3 == 0 :
      count_list.append((cnt+1) + num//3)
    cnt += 1
if len(count_list)==0 : print(-1)
else : print(min(count_list))