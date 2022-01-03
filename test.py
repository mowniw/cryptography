import math

def scrambler_first(chislo,next_1_):
    out=''
    for i in chislo:
        out.append(chislo[i])
        
    
        
                    
#def scrambler_last(chislo):  

def multiplyy(a,b):
    x=[0]*len(a)
    for i in range(len(a)):
        x[i]=a[i]*b[i]
    return(x)#(x[::-1])

#def moving(a,b):
    
def splitter(n):
    x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    return(x)

scr=open('scrembler.txt','r')



a=scr.read()
print(a)
#print(bin(int(a)))

n = 1101100
n = 1001111
#print(n)
#x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
#print(splitter(n))

AAA=[1, 0, 0, 0, 0, 1, 1]
BBB=[1, 0, 0, 1, 1, 1, 1]   #scrambler


AAA=[1,2,3,4,5,6,7]
BBB=[8,9,10,11,12,13,14]
temp=0
FINAL=[15]*len(AAA)

AAA=multiplyy(AAA,BBB)
print(AAA)
temp1=AAA[0]
temp2=15
#for i in range(1,len(AAA)-1):
    ##if i=0:
      ##  AAA[i]=
   # if i!=6:
     #   AAA[i]=temp1
      #  temp2=AAA[i+1]
      #  AAA[i+1]=AAA[i]
 #   else:
    #    FINAL[i]=AAA[i]
  #  #print(multiplyy(AAA,BBB))
   # #AAA=multiplyy(AAA,BBB)
    
   # #print()
##print('strange:',multiplyy(AAA,BBB))
#print('final:',FINAL[::-1])




