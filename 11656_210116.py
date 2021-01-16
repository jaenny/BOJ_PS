s=input()
L=[]
for i in range(len(s)) :
  new=s[i:]
  L.append(new)
L.sort()
for item in L :
  print(item)