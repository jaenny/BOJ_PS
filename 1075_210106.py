def find(n,f) :
  if n % f == 0 :
    return n
  else :
    return find(n+1,f)

n=input()
n2=int(n[:-2]+'00')

f=int(input())

print(str(find(n2,f))[-2:])