s=input()
L=[]
cnt = 0

for i in s :
  if i in "ABCDEFGHIJKLNMOPQRSTU" :
    L.append(i) #대문자들만 추가

for i in L :
  if i == 'U' and cnt == 0 : cnt += 1
  if i == 'C' and cnt == 1 : cnt += 1
  if i == 'P' and cnt == 2 : cnt += 1
  if i == 'C' and cnt == 3 : cnt += 1
  if cnt == 4 : break

if cnt == 4 : print('I love UCPC')
else : print('I hate UCPC')