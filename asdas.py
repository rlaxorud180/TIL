a="AABCDD"
b="afzz"
c="09121"
d="a8EWg6"
e="P5h3kx"

a_list=["*"]*15
for i,j in enumerate(a):
    a_list[i]=j

b_list=["*"]*15
for i,j in enumerate(b):
    b_list[i]=j

c_list=["*"]*15
for i,j in enumerate(c):
    c_list[i]=j

d_list=["*"]*15
for i,j in enumerate(d):
    d_list[i]=j

e_list=["*"]*15
for i,j in enumerate(e):
    e_list[i]=j

tmp=""
for i in range(0,15):
    if a_list[i]=="*" :
        a_list[i]="" 
    if b_list[i]=="*" :
        b_list[i]=""
    if c_list[i]=="*" :
        c_list[i]=""
    if d_list[i]=="*" :
        d_list[i]=""
    if e_list[i]=="*" :
        e_list[i]=""

    tmp=tmp+a_list[i]+b_list[i]+c_list[i]+d_list[i]+e_list[i]


print(tmp)


    
