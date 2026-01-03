# 오량
# Gold 2, combinatorics, modular multiplicative inverse

import sys
input = sys.stdin.readline
MOD = 10**9+7
MAX = 2000

def nCr(n,r):
    return fac[n]*ifac[n-r]*ifac[r]%MOD

fac = [1]
for i in range(1,MAX+1):
    fac.append(fac[-1]*i%MOD)
ifac = [1]*(MAX+1)
ifac[-1] = pow(fac[-1],-1,MOD)
for i in range(MAX,0,-1):
    ifac[i-1] = ifac[i]*i%MOD

for _ in range(int(input())):
    N = int(input())
    A = tuple(map(int,input().split()))

    if set(A) == {1}:
        print(1)
        continue

    result = 1
    c = N
    for a in A:
        result = result*nCr(c,a)%MOD
        c -= a
    print(result)