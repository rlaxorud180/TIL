#삽입 정렬

def insert_sort(a):
    flag=0
    while True:
        print(a)
        
        min_num=a[flag]  ## 밖에서 선언해야 for문 돌면서 바뀌지 않는다. 
        
        for i in range(flag,len(a)-1):
            
           
            if min_num>=a[i+1]:
                
                
                min_num=a[i+1]
                
                tmp=a[flag]    ## 리스트 스위칭 해줄떄는 tmp를 이용한다.
                               ## 같은 숫자가 있을때 index() 사용조심 사용안할듯
                a[i+1]=tmp
                a[flag]=min_num
      
      
        
       
       
        flag=flag+1
       
        
       
        if flag==len(a)-1:
            break

    print(a)


insert_sort([6,1,5,3,2,1,3])
        

    
        
        
