n=input().replace('6','9') #6이랑 9는 동일하게 취급
n=list(map(int,n)) #숫자 하나씩 쪼개기
set_n = set(n) #중복제거
dic_n = {}

for i in set_n :
  dic_n[i] = n.count(i) #몇번 등장하는지 사전에 저장

if 9 in dic_n and dic_n[9] >= 2 : #9가 두번 이상 등장한다면? -- > 한번으로 처리
  if dic_n[9] % 2 == 0 :
    dic_n[9] = dic_n[9]//2
  else :
    dic_n[9] = dic_n[9]//2 + 1

print(max(dic_n.values())) 
#가장 count가 많은 수를 출력해야함
#왜?
#만약 1111666이라면 1이 4번 쓰이기 때문에 4세트 필요 666은 겨우 2세트 필요
#따라서 가장 많이 쓰이는 수가 출력되어야함.