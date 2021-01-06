import sys
t = int(sys.stdin.readline())
cnt = 0
for i in range(t) :
  cnt = 0
  s=list(map(str,sys.stdin.readline()))
  check = s.copy()
  check.reverse()
  if s == check :
    print(0)
  else :
    for i in range(len(s)//2) :
      if s[i] == s[len(s)-1-i] :
        continue
      else :
        if s[i] == s[len(s)-2-i] :
          s.pop(s.index(s[len(s)-1-i]))
          cnt += 1 
        elif s[i+1] == s[len(s)-1-i] :
          s.pop(s.index(s[i]))
          cnt += 1 
        else : cnt +=2
  if cnt == 1 :print(1)
  elif cnt != 0 : print(2)