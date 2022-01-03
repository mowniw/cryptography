def a_new_addition(a):
    k=0
    for i in range(len(a)):
        k+=a[i]
    return(k%2)

def modul_2(a,b):
    c='';d=''
    CD=0
    CD1=[0]*7
    CD2=[0]*7
    for i in range(7):
        #c=c+str(a[i])
        #d=d+str(b[i])
        pass

    #CD=int(a)^int(d)
    CD=binaryy(a^int(b))
    #print(CD)
    CD1=splitter(int(CD))
    return(CD1)



binscr=[1,0,0,1,1,1,1]
a_new=[1,0,0,0]

print(13 // 3)
print(13 % 3)

print(a_new_addition(binscr))
