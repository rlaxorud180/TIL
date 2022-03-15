
def itoa(a):
    tmp=0
    main_tmp=""
    flag=0
    if a<0:
        a=-a
        flag=1
        
    while a>0:
        tmp=a%10
        a=a//10
        main_tmp=chr(48+tmp)+main_tmp #chr(48)이 문자값으로 0을 가지므로 기본값으로 활용

    if flag==1:
        main_tmp=chr(45)+main_tmp
        
    return main_tmp

for tc in range(1,7):
    a=int(input())

    print(f"#{itoa(a)} {type(itoa(a))}")
    

        


