def connectorr(a):
    ans=''
    for i in range (len(a)):
        ans+=str(a[i])
    ansver=int(ans,2)
    return(ansver)
        
                    

#a=input()
#a='1000001'
a=[1, 0, 0, 0, 0, 0, 1]
#print(int(a,2))

print(connectorr(a))
