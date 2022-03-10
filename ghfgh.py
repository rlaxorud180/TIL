t=int(input())

for tc in range(t):
    
    a=list(map(int,input().split()))
    n=int(input())
    b=[]
    for i in range(n):
        c=list(map(int,input().split()))
        b=b+[c]
    

    def start_area(*b):
        global a
        
        radius=pow((((a[0]-b[0][0])**2)+((a[1]-b[0][1])**2)),0.5)

        if radius < b[0][2]:
            return True

        else:
            return False



    def end_area(*b):
        global a
        
        radius=pow((((a[2]-b[0][0])**2)+((a[3]-b[0][1])**2)),0.5)

        if radius < b[0][2]:
            return True

        else:
            return False
        
    count=0
    for i in b:
        
        if start_area(i)!=end_area(i):
            count=count+1

        
        
    print(count)   
    
