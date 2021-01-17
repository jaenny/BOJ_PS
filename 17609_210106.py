def pal(s) :
  check = s.copy()
  check.reverse()
  if s == check :
    return 1
  else :
    return 0

t = int(input())
for i in range(t) :
  s=list(map(str,input()))
  if pal(s) == 1 : #펠린드롬인지 체크
    print(0)
  else :
    for i in range(len(s)//2) :
      if s[i] != s[len(s)-1-i] : #양 끝이 달라지는 부분 체크
        break
    if pal(s[i+1:len(s)-i]) == 1 : #왼쪽에서 하나 떼고 펠린드롬인지 체크 --> 맞다면 유사회문
      print(1)
    elif pal(s[i:len(s)-i-1]) == 1 : #오른쪽에서 하나 떼고 펠린드롬인지 체크 --> 맞다면 유사회문
      print(1)
    else : print(2) #둘 다 아닌 경우
