w=input().lower()
L={}
for i in range(len(w)):
  if w[i] in L :
    L[w[i]]=L[w[i]]+1
  else : 
    L[w[i]]=1

L_list = list(L) #가장 첫 값을 max로 설정하기 위해 key값으로만 이루어진 리스트 생성
max = L[L_list[0]]
max_word=L_list[0]
cnt=0 #cnt 초기화

for i in range(len(L)): #가장 많이 등장하는 단어 탐색
  if L[L_list[i]] > max :
    max= L[L_list[i]]
    max_word=L_list[i]
    cnt=1

for i in range(len(L)): #?가 나오는 상황 찾기 위해
  if L[L_list[i]]==max :
    if L_list[i] != max_word :
      cnt=2

if cnt == 2: print('?')
else : print(max_word.upper())