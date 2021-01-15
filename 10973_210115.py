n=int(input())
perm=[int(x) for x in input().split()]

check=sorted(perm.copy())
lst=[]
if perm == check :
  print(-1)
else :
  minimum = perm[-1]
  for i in range(len(perm)) :
    lst.append(perm[len(perm)-1-i])
    if perm[len(perm)-1-i] > minimum :
      flag = perm[len(perm)-1-i]
      break
    else :
      minimum = perm[len(perm)-1-i]
  lst.reverse()

if len(lst) == 0 :
  pass
else :
  lst.sort()
  next_flag = lst[lst.index(flag)-1]
  lst.remove(next_flag)
  lst.sort(reverse=True)
  perm=perm[0:perm.index(flag)]
  perm=perm+[next_flag]+lst
  for i in perm:
    print(i,end=' ')


