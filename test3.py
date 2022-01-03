import math
def scrambler_first(chislo,next_1_,i):
    out=chislo
    #for i in chislo:
     #   out.append(chislo[i])
    out.insert(i,next_1_)
    return(out)

def binaryy(i):
    b=''
    while i>0:
        b=str(i%2)+b
        i=i//2
    return(b)

def splitter(n):
    x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    return(x)


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

def modul_2(a,b):
    c='';d=''
    CD=0
    CD1=[0]*7
    CD2=[0]*7
    for i in range(7):
        c=c+str(a[i])
        d=d+str(b[i])

    CD=int(c)^int(d)
    CD1=splitter(CD)
    return(CD1)
        
    
        
    
#for i in range(5):
    #b.append(a[i])
  #  print(i)
   # b.insert(i,a[i])

FINAL=[0]*7

a=[1,2,3,4,5,6,7]   #scrambler
a_new=[8, 18, 30, 44, 60, 78, 98]
b=[8,9,10,11,12,13,14]
print('b start',b)
#b=scrambler_first(b,a[0],0)
#print('1',b)
#FINAL[0]=scrambler_last(b)
#print('fi_1',FINAL)
#b=scrambler_cut(b)
#print('b',b)
#print('fin',FINAL)

for i in range (7):
    b=scrambler_first(b,a_new[0],i)
    FINAL[i]=scrambler_last(b)
    b=scrambler_cut(b)
    #тут добавить перевод в десятичную,через def
    a_new=modul_2(b,a)
    
print('b end',b) 
print(FINAL)
