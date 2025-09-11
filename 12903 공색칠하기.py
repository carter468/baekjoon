# 공 색칠하기
# Gold 2, math, combinatorics

import sys
input = sys.stdin.readline
MOD = 10**9+7

def ncr(n,r):
    if r*2 > n: r = n-r
    x = 1
    for i in range(r):
        x = x*(n-i)//(i+1)
    return x%MOD

result = 1
t = 0
for _ in range(int(input())):
    c = int(input())
    result = result*ncr(t+c-1,t)%MOD
    t += c
print(result)