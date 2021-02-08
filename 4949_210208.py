while True :
  s = input()
  if s == '.' : break
  stack=[]
  for i in s :
    if i=='(' : stack.append('(')
    elif i=='[' : stack.append('[')
    elif i==')' :
      if len(stack)==0 : stack.append(')')
      else :
        if stack[-1]=='(' : stack.pop()
        else : stack.append(')')
    elif i==']' :
      if len(stack)==0 : stack.append(']')
      else :
        if stack[-1]=='[' : stack.pop()
        else : stack.append(']')
  
  if len(stack)==0 : print('yes')
  else : print('no')