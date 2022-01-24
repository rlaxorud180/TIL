def number(a):
    tmp_main=0
    b=str(a)
    count=1
    while count <=len(b):
        print(a)
        tmp=a%10
        
        tmp_main=tmp_main*10+tmp
        a=a//10
        count=count+1





    return tmp_main










print(number(123456))