import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp=[1]*n

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j] :
            dp[i]=max(dp[i],dp[j]+1)


print(max(dp))

tmp=[]
count=max(dp)
for i in range(n-1,-1,-1):
    if dp[i]==count:
        tmp.append(a[i])
        count=count-1
print(*reversed(tmp))
