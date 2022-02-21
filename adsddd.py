a=["a","a","a"]
b=["a","a","b"]
c=["a","b","c","b","a"]
d=["a","b","b","a"]

def palim(a):
    n=int(len(a)/2)
    for i in range(n):
        
        if a[i]!=a[-1-i]:
            return 0
    else:
        return 1


print(palim(a))
print(palim(b))
print(palim(c))
print(palim(d))
