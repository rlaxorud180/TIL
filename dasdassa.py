a=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i> j:
            a[i][j], a[j][i]= a[j][i],a[i][j]

print(a)
