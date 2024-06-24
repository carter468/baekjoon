# Σ
# Gold 4, FLT, exponentiation by squaring, modular multiplicative inverse

import sys
input = sys.stdin.readline

M = 10**9+7

result = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    result = (result+pow(a,-1,M)*b)%M
print(result)