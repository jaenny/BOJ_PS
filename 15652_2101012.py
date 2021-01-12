n,m=map(int,input().split())
visit=[0]*100
my_vec =[]
def Com(now, cnt):
    if(cnt==m):
        for i in my_vec:
            print(i,end=' ')
        print()
        return
    for i in range(now,n+1):
        my_vec.append(i)
        Com(i,cnt+1)
        my_vec.pop()

Com(1,0)