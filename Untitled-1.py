def dict_invert(my_dict):
    reverse_dict={}

    tmp_key=[]
    tmp_value=set()
    for i,j in my_dict.items():   
        tmp_key.append(i)
        tmp_value.add(j)       ##{1:10, 2:20, 3:30, 4:20, 5:10, 6:40}
    
    tmp_value=list(tmp_value)
    main_tmp=[]
    for i in tmp_value:  #[10,20,30,40]
        tmp=[]
        for j in tmp_key:
            
            if my_dict[j]==i:
                tmp.append(j)
       
        main_tmp=main_tmp+[tmp]
     
    
    for i,j in enumerate(tmp_value):
        reverse_dict[j]=main_tmp[i]

    print(reverse_dict)
   
print(dict_invert({1:10, 2:20, 3:30, 4:20, 5:10, 6:40}))