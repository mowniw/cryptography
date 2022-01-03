def multiplyy(a,b):
    x=[0]*len(a)
    for i in range(len(a)):
        x[i]=a[i]*b[i]
    return(x)#(x[::-1])


AAA=[1, 0, 0, 0, 0, 1, 1]
BBB=[1, 0, 0, 1, 1, 1, 1]


AAA=multiplyy(AAA,BBB)
a=AAA.pop
#print(a)


length = 7#int(input())
lst = list(map(int, input().split()))
shift = 2#int(input())

lst = lst[-shift:] #+ lst[:-shift]

print(lst)
