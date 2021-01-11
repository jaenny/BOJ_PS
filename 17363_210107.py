def change(L) :
  if '-' in L :
    L=L.replace('-','45')
  if '|' in L :
    L=L.replace('|','-')
  if '45' in L :
    L=L.replace('45','|')
  if '/' in L :
    L=L.replace('/','47')
  if "\\" in L :
    L=L.replace("\\","/")
  if '47' in L :
    L=L.replace('47','\\')
  if '^' in L :
    L=L.replace('^','94')
  if '<' in L :
    L=L.replace('<','60')
  if 'v' in L :
    L=L.replace('v','118')
  if '>' in L :
    L=L.replace('>','62')
  if '94' in L :
    L=L.replace('94','<')
  if '60' in L :
    L=L.replace('60','v')
  if '118' in L :
    L=L.replace('118','>')
  if '62' in L :
    L=L.replace('62','^')
  return L

n,m=input().split()
n=int(n); m=int(m)
L=[]
for i in range(n) :
  L.append([])
  s=input()
  s=change(s)
  l=list(map(str,s))
  L[i].extend(l)

for i in range(m) :
  for j in range(n) :
    print(L[j][m-1-i],end='')
  print('')
