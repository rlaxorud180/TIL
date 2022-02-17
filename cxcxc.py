def baby_gin(a):
    
    count=0
    for i in a:
        if a.count(i)==3 or a.count(i)==6:
            a.remove(i)
            a.remove(i)
            a.remove(i)
            count=count+1


    if count==2:
        return 1
   
    flag=0
    
    if len(a)==3:
        for i in a[0:2]:
       
            if i+1 in a:
                flag=1
            else:
                flag=0
                break
       
        
    
    
    if len(a)==6:
        a=set(a)
        
        a=list(a)
            
        for i in a[0:len(a)-1]:
            if i+1 in a:
                
                flag=2
            else:
                flag=0
                break
        

    if flag==1:
        count=count+1
    elif flag==2:
        count=2
    else:
        count=0
            
    
            
    if count==2:
        return 1
    else:
        return 0

print(baby_gin([1,1,2,2,3,3]))
        


    
        


