# 버블 정렬

list1=[7,5,9,0,3,1,6,2,4,8]

def insert_sort(a):
    list_len=len(a)
   
    for i in range(1,list_len):
       
        while True:
            if a[i-1]>=a[i]:
               
                a[i-1],a[i]=a[i],a[i-1]
                i=i-1
                if i==0:
                    break
            else:
                
                break
            

    print(a)
        
    
    

insert_sort(list1)
                
