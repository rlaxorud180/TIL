
M="OOXXOXXOOO"#str(input())


tmp=0
result=0
number_count=0

for i in M:
    number_count=number_count+1
    
    if i=="O":
        tmp=tmp+1
    
    elif i=="X" and tmp !=0:

        count=0
            
        for j in range(1,tmp+1):
            count=count+j
        result=result+count
        tmp=0

    
    if  number_count==len(M):
        count=0
            
        for j in range(1,tmp+1):
            count=count+j
        result=result+count
        tmp=0

print(result)
    
    







