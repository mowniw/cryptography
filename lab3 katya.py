import random
from random import getrandbits
from random import randint
import sys
import time
def fast_pow(x,y):
    if y==0:
        return 1
    if y==-1:
        return 1./x
    p=fast_pow(x,y//2)
    p*=p
    if y%2:
        p*=x
    return p

def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return(a)

def is_prime(n):
    print('test,n=',n)
    if n!=int(n):
        return False
    n=int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True
    s=0
    d=n-1
    while d%2==0:
        d>>1
        s+=1
    assert(2**s*d==n-1)
    
    def trial_composite(a):
        if pow(a,d,n)==1:
            return False
        for i in range(s):
            if pow(a,2**i*d,n)==n-1:
                return False
        return True

    for i in range(8):
        a=random.randrange(2,n)
        if trial_composite(a):
            return False
    print('test2')
    return True

def primitive_root(module):
    req_set=set(num for num in range(1,module)if gcd(num,module)==1)
    for g in range(1,module):
        act_set=set(pow(g,powers)% module for powers in range(1,module))
        if req_set==act_set:
            return g

def get_random_prime(t):
    while True:
        n=getrandbits(int(t))+3
        print(t)
        if is_prime(n):
            return n

t=input()
start_time=time.time()
print(get_random_prime(t))
print('длительность:',time.time()-start_time)
















    
