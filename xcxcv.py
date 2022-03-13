def strcmp(a,b):
    a_list=list(a)
    b_list=list(b)
    for i,j in enumerate(a_list):
        if ord(j)<97:
            a_list[i]=chr(ord(j)+32)

    for i,j in enumerate(b_list):
        if ord(j)<97:
            b_list[i]=chr(ord(j)+32)

    
    if len(a_list)>=len(b_list):
        min_i=len(b_list)
    else:
        min_i=len(a_list)

    i=0
    while True:
        if i==min_i:
            if len(a_list)>len(b_list):
                return b

            elif len(a_list)<len(b_list):
                return a
            elif len(a_list)==len(b_list) and a_list[i]==b_list[i]:
                return "same"
            
        if a_list[i]<b_list[i]:
            return a

        elif a_list[i]>b_list[i]:
            return b

        i=i+1
            

print(strcmp("po", "pl"))

            
            
