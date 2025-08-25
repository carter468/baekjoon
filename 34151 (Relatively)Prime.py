# (Relatively) Prime
# Platinum 5, number theory, modular multiplicative inverse, exponentiation by squaring

import sys
input = sys.stdin.readline
MOD = 998244353

for _ in range(int(input())):
    p,n,m = map(int,input().split())
    if n > m: n,m = m,n
    if n != m:
        a = pow(p,n,MOD)
        b = (m-1)//n
        if a == 1:
            print((b+pow(p,m,MOD))%MOD)
        else:
            print((a*pow(a-1,-1,MOD)*(pow(a,b,MOD)-1)+pow(p,m,MOD))%MOD)
    else:
        print(pow(p,n,MOD))