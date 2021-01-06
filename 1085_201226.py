L=[int(x) for x in input().split()]
if L[0]<L[2]-L[0] : x=L[0]
else : x=L[2]-L[0]

if L[1]<L[3]-L[1] : y=L[1]
else : y=L[3]-L[1]

print(min(x,y))