# 아파트 임대
# Platinum 1, 밀러-라빈 소수 판별법

import random

def miller_rabin(n,b,k,m):
    x = pow(b,m,n)
    if x==1 or x==n-1:
        return 1
    for _ in range(k):
        if x==n-1:
            return 1
        x = pow(x,2,n)
    return 0

def is_prime(n):
    if n<2 or not n&1:
        return 0
    if n==2 or n==3:
        return 1
    k=0
    m=n-1
    while m%2==0:
        k+=1
        m>>=1
    for _ in range(3):  # 3은 조절 가능한 값
        if miller_rabin(n,random.randrange(2,n-1),k,m)==0:
            return 0
    return 1

answer = 0
for _ in range(int(input())):
    answer += is_prime(int(input())*2+1)
print(answer)