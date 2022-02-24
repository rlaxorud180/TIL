a="abbc"
b="abbbbabc"

num=len(b)-len(a)+1

flag=0
for i in range(1,num+1):
    for j,k in enumerate(a):
        if k!=b[j]:
            b=b[1::]
            break
    else:
        flag=1
        print(flag)
else:
    print(flag)
