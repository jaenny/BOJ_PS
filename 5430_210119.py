T=int(input())
for i in range(T) :
  cnt = 0 #R의 개수를 담을 변수
  flag = 0
  p=input(); pcnt=p.count('R'); dcnt=p.count('D')
  n=int(input())
  arr=input();
  if n == 0 : 
    flag=2
  else :
    arr=arr[1:-1]
    arr=list(map(int,arr.split(',')))
  arr=list(arr)
  for j in range(len(p)) :
    #R이 들어올 때 마다 cnt++해줘서
    #cnt가 짝수이면 앞에서 D를 수행하고
    #cnt가 홀수이면 뒤에서 D를 수행
    if p[j] == 'D' and len(arr) == 0 : #arr이 비었는데 D를 시도한 경우 --> error
      flag = 1
      break
    if p[j] == 'R' : 
      cnt += 1
      continue
    else : #D
      if cnt % 2 == 0 :
        arr.pop(0)
      else :
        arr.pop(-1)

  if flag == 0 :
    if len(arr) == 0 : print('[]')
    elif cnt % 2 == 1 : #R이 홀수개
      arr.reverse()
      print('['+','.join(str(x) for x in arr)+']')
    else : #R이 짝수개
      print('['+','.join(str(x) for x in arr)+']')
  elif flag == 2 and dcnt == 0 : print('[]') #D가 없고 n으로 0이 들어왔을 때
  elif flag == 2 or flag == 1: print("error") #D가 있으면서 n으로 0이 들어오는 경우 or 빈 arr에서 D를 시도한 경우