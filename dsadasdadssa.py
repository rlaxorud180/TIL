arr=[3,6,7,1,5,4]


n=len(arr)
tmp=0
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            
            print(arr[j],end=",")


    print()
print()



##부분집합들의 
##arr=[3,6,7,1,5,4]
##
##
##n=len(arr)
##
##for i in range(1<<n):
##    tmp=0
##    for j in range(n):
##        if i&(1<<j):
##            tmp=tmp+arr[j]
##    print(tmp)
