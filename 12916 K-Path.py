# K-Path
# Gold 1, 분할정복 거듭제곱

import sys
input = sys.stdin.readline
MOD = 10**9+7

def mul(a,b):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += a[i][k]*b[k][j]%MOD
            c[i][j] = temp%MOD
    return c

def pow(a,x):
    if x <= 1:
        return a
    b = pow(a,x//2)
    return mul(b,b) if x%2==0 else mul(mul(b,b),a)
    
n,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

result = 0
for i in pow(arr,k):
    result += sum(i)%MOD

print(result%MOD)