import math

def scrambler_first(chislo,next_1_,i):
    out=chislo
    #for i in chislo:
     #   out.append(chislo[i])
    out.insert(i,next_1_)
    return(out)

def scrambler_last(chislo):
    k=0
    for i in chislo:
        k+=1
        #print(k)
    return(chislo[k-1])

def scrambler_cut(chislo):
    k=0
    for i in chislo:
        k+=1
    b=[0]*(k-1)
    for i in range(k-1):
        b[i]=chislo[i]
    return(b)

def binaryy(i):
    b=''
    while i>0:
        b=str(i%2)+b
        i=i//2
    return(b)

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




def splitter(n):
    x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    return(x)

def multiplyy(a,b):
    x=[0]*len(a)
    for i in range(len(a)):
        x[i]=a[i]*b[i]
    return(x)#(x[::-1])

def connectorr(a):             #собирает массив в одно число и переводит его в 10
    ans=''
    for i in range (len(a)):
        ans+=str(a[i])
    ansver=int(ans,2)
    return(ansver)

text=''
b=''

binInp=[]
numberInp=[]
binscr=[]


simv=0
simv_t=0



scr=open('scrembler.txt','r')
text_in=open('input.txt','r')



#for i in scr.read():
    #print(i)
    #a.append(i)
   # b=b+i
    #numberInp.append(ord(i))
    #binscr.append(binaryy(int((ord(i)))))
    #simv+=1

b=scr.read()
binscr=binaryy(int((b)))
print('Вводимый скремблер:',b)#,'символов:',simv)
print('Вводимый скремблер в двоичном виде:')
print(binscr)
binscrsplit=splitter(int(binscr))              #scrambler

for i in text_in.read():
    #print(i)
    #a.append(i)
    text=text+i
    numberInp.append(ord(i))
    binInp.append(binaryy(int((ord(i)))))
    simv_t+=1
#print(a)
print('Вводимый текст:',text)#,'символов:',simv)
print('Вводимый текст в десятичном виде:',numberInp)
print('Вводимый текст в двоичном виде:')
print(binInp)

abcc=[0]*(simv_t)#да,я решил написать комментарий(сейчас 2 ночи).Это
                 #переменная является массивом элементы которого являются мас-
                 #сивами с символами.Да.
print()
for i in range(simv_t):
    #print(binInp[i])
    print(splitter(int(binInp[i])))
    abcc[i]=splitter(int(binInp[i]))
#print(binInp[1])
print(abcc)
print()
for i in range(simv_t):
    for j in range(len(binInp[1])):#simv_t):
        #print('i:',i,', j:',j,', abcc:',abcc[i][j])
        pass
    print()
#print(abcc[0][1])

print('simvolov:,',simv_t)
for i in range(simv_t):
    print(abcc[i])
print('binscr',binscrsplit)

#abcc[i]-это первое бинарное число.Скремблер сверху.a_new-это результат
#мультиплая или сложения по модулю2 
FINAL=[0]*7
k=0
a_new=multiplyy(abcc[0],binscrsplit)
print('a_new',a_new)
for i in range(7):
    print('цикл ',i)
    print('abcc[k]',abcc[k],' FINAL[i]',FINAL[i],' temp','temp',' a_new',a_new)
    abcc[k]=scrambler_first(abcc[k],a_new[0],i)
    #FINAL[i]=scrambler_last(abcc[k])
    FINAL[i]=scrambler_last(a_new)
    abcc[k]=scrambler_cut(abcc[k])
    temp=connectorr(abcc[k])
    print('vot tut',temp,b)
    a_new=modul_2(temp,b)#b-это скремблер в десятичном виде,запомни!!!
    print('abcc[k]',abcc[k],' FINAL[i]',FINAL[i],' temp',temp,' a_new',a_new)
print('final input:',abcc[0])
print('final FINAL:',FINAL)
