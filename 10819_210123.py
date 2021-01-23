n=int(input())
arr=sorted(list(map(int,input().split())))

def next_permutation(lst):
    n = len(lst)
    i = n - 1
    while i > 0 and lst[i - 1] >= lst[i]:
        i -= 1
    if i == 0:
        return [-1]
    j = n - 1
    while lst[j] <= lst[i - 1]:
        j -= 1
    tmp = lst[j]
    lst[j] = lst[i - 1]
    lst[i - 1] = tmp

    lst = lst[:i] + sorted(lst[i:])
    return lst

maximum = -99999999
while True :
  if arr == [-1] : break
  ans = 0
  for i in range(n-1) :
    ans = ans + abs(arr[i] - arr[i+1])
  if ans > maximum :
    maximum = ans
  arr = next_permutation(arr)

print(maximum)




"""
small=[]
big=[]
res=[]
for i in range(int(len(arr)/2)) :
  small.append(arr[i])
  big.append(arr[len(arr)-1-i])
if len(arr)%2 != 0 :
  big.append(arr[int(len(arr)/2)])

if n==3 and big[1] - small[0] < big[0] - big[1]:
  res.append(big.pop(0))
  res.append(small.pop(0))
  res.insert(0,big.pop(0))
else : 
  res.append(small.pop(0))
  res.append(big.pop(0))
  res.insert(0,big.pop(0))

while True :
  if len(small) == 0 and len(big) == 0 : break
  if len(small) != 0 :
    new = small.pop(0)
    if abs(new-res[0]) < abs(res[-1] - new) : res.append(new)
    elif abs(new-res[0]) == abs(res[-1] - new) : 
      if res[0] < res[-1] : res.append(new)
      else : res.insert(0,new)
    else : res.insert(0,new)
  if len(big) != 0 :
    new = big.pop(0)
    if abs(new-res[0]) < abs(res[-1] - new) : res.append(new)
    elif abs(new-res[0]) == abs(res[-1] - new) : 
      if res[0] > res[-1] : res.append(new)
      else : res.insert(0,new)
    else : res.insert(0,new)

ans=0
for i in range(n-1) :
  ans = ans + abs(res[i]-res[i+1])
print(res,ans)
"""