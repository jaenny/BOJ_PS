for x in range(int(input())) :
  s=input()
  cnt=0
  while '()' in s :
    cnt+=1
    for i in range(len(s)) :
      if '()' in s :
        if s[i]=='(' and s[i+1] == ')' :
          s=s[:i]+s[i+2:]
          break
      else : 
        break
  if cnt >0 and len(s) >0 : print("NO")
  elif cnt == 0 : print("NO")
  elif cnt >0 and len(s)==0 : print("YES")