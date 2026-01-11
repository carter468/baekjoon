# 이집트 분수
# Gold 5, math

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

while True:
    m,n = map(int,input().split())
    if m == 0: break

    while m > 1:
        i = n//m+1
        while True:
            x = n*i
            y = m*i-n
            g = gcd(x,y)
            y //= g
            x //= g
            if x < 10**6:
                print(i,end=' ')
                n,m = x,y
                break
            i += 1
    print(n)