n=int(input())

dp=[0]*(n+1)
mul=[0]*(n-3) #dp가 몇 번 곱해지는 것이 최대의 결과를 가져오는지 저장할 배열

#mul 배열 계산하기
for i in range(1,n-3) :
  if i< 6 : 
    mul[i] = i+1
  else : 
    mul[i] = (i-3)*3

#dp배열 채우기
for i in range(1,n+1) :
  if i <= 6 :
    dp[i] = i
  else : #n이 7이상일 경우
    temp = []
    j=1
    while i-2-j != 2 :
      temp.append(dp[i-2-j]*mul[j])
      j+=1
    dp[i] = max(temp)

print(dp[-1])


