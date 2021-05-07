n=int(input())
m=int(input())

enable = {str(i) for i in range(10)}  # 0, 1, 2 ... 9 (가능한 수)

if m != 0:
  broken = set(map(int, input().split()))
else : broken=set()
#+,-로만 움직이기
min_cnt = abs(100-n)

#숫자 입력과 +,-
#500,000채널에 가야하는데 5,6,7,8,9가 모두 망가진 경우라면 1,000,000에서 시작해야함
for num in range(1000001) :
  num = str(num)
  for j in range(len(num)) :
    if int(num[j]) in broken : #번호를 눌러서 올 수 없다면
      break
    elif j == len(num) - 1 :
      min_cnt = min(min_cnt,abs(n - int(num)) + len(str(num)))
print(min_cnt)
