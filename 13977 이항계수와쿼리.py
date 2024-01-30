# 이항 계수와 쿼리
# Platinum 5, math, FIT, exponentiation by squaring, modular multiplicative inverse

import sys
input = sys.stdin.readline
MOD = 10**9+7

arr = [1]
for i in range(1,4000001):
    arr.append(arr[-1]*i%MOD)

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(arr[n]*pow(arr[k]*arr[n-k],MOD-2,MOD)%MOD)