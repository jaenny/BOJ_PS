n=int(input())
arr=[int(x) for x in input().split()]
b,c=map(int,input().split())

count=0
#한 시험장에는 꼭 총감독관이 한명은 들어간다
count = count + len(arr)


for student in arr :
  if student - b > 0 :
    if (student-b)%c != 0 :
      count = count + ((student-b)//c)+1
    else :
      count = count + ((student-b)//c)

print(count)