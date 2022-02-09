a=[1,2,3]
b=[1,2]

def ab(*a):
    global b
    c=a[0][1]+b[1]

    return c


print(ab(a))
