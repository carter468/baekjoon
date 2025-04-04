# pn!과 쿼리
# Gold 3, exponentiation by squaring, modular multiplicative inverse

import sys
input = sys.stdin.readline
MOD = 10**9+7

for _ in range(int(input())):
    p,n = map(int,input().split())

    print((pow(p,n,MOD)-1)*pow(p-1,MOD-2,MOD)%MOD)