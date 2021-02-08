L =[3, 10, 1, 9, 43, 27, 5]
print(L)
for x in L :
    if x % 3 == 0 :
        a = L.index(x)
        L[a:a+1] = [x * 10]
print(L)
