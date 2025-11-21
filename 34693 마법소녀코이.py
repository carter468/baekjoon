# 마법소녀 코이
# Gold 4, constructive, ad hoc

import sys
input = sys.stdin.readline

p,m = '+','-'

for _ in range(int(input())):
    k = int(input())

    a = int(k**0.5)+1
    d = a*a-k
    if d == 1:
        a += 1
        d = a*a-k

    if d == 0: 
        print(a,p,1,m,1)
    elif d%2 == 1:
        b = d//2
        c = d-b
        print(a,p,b,m,c)
    else:
        a += 1
        d = a*a-k
        b = d//2
        c = d-b
        print(a,p,b,m,c)