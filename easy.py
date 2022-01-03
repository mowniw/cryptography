import random



def binaryy(i):
    b=''
    while i>0:
        b=str(i%2)+b
        i=i//2
    return(b)
        


file=open('input.txt','r')
out_key=open('key.txt','w')
out_res=open('result.txt','w')

numberInp=[]
binInp=[]

key=[]
keySim=''
key_bin=[]

res=[]
resSim=''
res_bin=[]

b=''
#cl=ml=0

simv=0
for i in file.read():
    #print(i)
    #a.append(i)
    b=b+i
    numberInp.append(ord(i))
    binInp.append(binaryy(int((ord(i)))))
    simv+=1
#print(a)


print('Вводимый текст:',b)#,'символов:',simv)
print('Вводимый текст в десятичном виде:',numberInp)
print('Вводимый текст в двоичном виде:')
print(binInp)
#print(numberInp)



print()
print()


a=0
k=0
while a==0:
    
    while k<simv:
        #c=random.uniform(33,
        c=33+(int(random.uniform(1,100)*1000))%80
        #print(c)
        key.append(c)
        keySim+=chr(int(c))
        key_bin.append(binaryy(int(c)))
        k+=1
    print('полученый ключ:',keySim)#,'     ',key)
    print('полученый ключ в десятичном виде:',key)
    print('полученый ключ в двоичном виде:')
    print(key_bin)
    print('хотите изменить ключ?0=нет')
    ans=input('')
    if ans=='0':
        a=1

print()
print()


d=0
while d<simv:
    res.append(numberInp[d]^key[d])
    resSim=resSim+(chr(numberInp[d]^key[d]))
    res_bin.append(binaryy(numberInp[d]^key[d]))
    d+=1

print('полученый результат:',resSim)
print('полученый результат в двоичном виде:')
print(res_bin)
print('полученый результат в десятичном виде:')
print(res)
    




out_res.write(resSim)    
out_key.write(keySim)







out_res.close()
out_key.close()
