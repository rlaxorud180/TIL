n=5
k=10

number_list=[x for x in range(1,13)]
count=0

for i in range(1,14-n):
    if sum(number_list[i-1:i+n-1])==k:
        tmp_main=number_list[i-1]
    else:
        tmp_main=False
        

print(tmp_main)
if tmp_main == True:
    if tmp_main==k:
        count=1
    else:
        count=tmp_main
else:
    count=0
