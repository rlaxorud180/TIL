check_list=["GOFFAKWFSM","OYECRSLDLQ",
"UJAJQVSYYC",
"JAEZNNZEAJ",
"WJAKCGSGCF",
"QKUDGATDQL",
"OKGPFPYRKQ",
"TDCXBMQTIO",
"UNADRPNETZ",
"ZATWDEKDQF"]
T=int(input())

for tc in range(1,T+1):
    N,M= map(int, input().split())
    check_list=[]
    check_list_turn=[]
    for i in range(0,N):
        check_list.append(str(input()))

    for i in range(0,N):
        tmp=""
        for j in range(0,N):
            tmp=tmp+check_list[j][i]
        check_list_turn.append(tmp)
            

    tmp_list=[]
    count=0
    while True:
        for i in range(count,count+M):
            if check_list[i]==check_list[i][::-1]:
                tmp_list.append(check_list[i])
                
            if count+M>N:
                break
            else:
                count=count+1
            
    count=0
    while True:
        for i in range(count,count+M):
            if check_list_turn[i]==check_list_turn[i][::-1]:
                tmp_list.append(check_list_turn[i])
                
            if count+M>N:
                break
            else:
                count=count+1
            

    print(f"#{tc} {tmp_list}")
