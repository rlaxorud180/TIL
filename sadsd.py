
a="this is the book"
b="is"

n=len(a)
m=len(b)

def brute(a,b):
    print(n)
    i=0
    j=0
    while i<n and j<m:
        if a[i]!=b[j]:
            i=i-j
            j=-1
        i=i+1
        j=j+1
    if j==m:
        return 1
    else:
        return 0


print(brute(a,b))
            
