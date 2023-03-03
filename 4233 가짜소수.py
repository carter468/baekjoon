# 가짜소수
# Gold 4, 소수판정, 분할정복

import sys

def is_prime(n):
    if n%2==0:
        return 0
    
    i = 3
    while i*i<=n:
        if n%i==0:
            return 0
        i += 2
    return 1

def apmp(a,n):
    if n==1:
        return a
    
    if n%2==0:
        return (apmp(a,n//2)**2)%p
    else:
        return (apmp(a,n//2)**2*a)%p
    
while 1:
    p,a = map(int,sys.stdin.readline().split())
    if p==0:
        break

    print('no' if is_prime(p) or apmp(a,p)!=a else 'yes')