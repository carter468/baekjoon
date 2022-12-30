# 최대 사이클 1
# Gold 3, 조합론

import sys
input = sys.stdin.readline

def nCr(n,r):
    return fac[n]//fac[n-r]//fac[r]

fac = [1]*20
for i in range(19):
    fac[i+1] = fac[i]*(i+1)

for _ in range(int(input())):
    n,k = map(int,input().split())

    result = 0
    for i in range(1,k+1):
        result += nCr(k-2,i-2)*fac[i-1]*fac[n-i]
    print(result)