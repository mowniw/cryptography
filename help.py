key=''
Scrambler='00100111'
a=''
result=''

file=open('inputScr.txt','w')
fileTXT=open('inputTEXT.txt','w')

print('Введите значение скремблера:')
Scr=input()
file.write(Scr)
n=len(Scr)

print('Введите текст для кодирования:')
inp=input()
fileTXT.write(inp)


print('скремблер в двоичной системе:')
print(Scr)
print('скремблер в десятичной системе:')
print(int(Scr,2))

for i in range(56):
    b='0'
    for k in range(len(Scrambler)-1,0):
        if (Scrambler[k]=='1'& Scr[k]=='0')|(Scrambler[i]=='0'&Scr[i]=='1'):
            if b=='0':
                b='1'
            else:
                b='0'
    key+=Scr[len(Scr)-1]
    Scr=b+Scr[:-1]
key2=[]
print('Итоговый ключ:',end='')
for i in range(len(key)):
    a+=key[i]
    print(key[i],end='')
    if i%8==0:
        print(end=' ')


print()
print('vvodimiy text')
for i in range(n):
    result+=chr(ord(Scr[i])^ord(key[i]))
print(result)
            
            

fileTXT.close()
file.close()
