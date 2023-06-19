# 수 고르기
# Gold 5, 투 포인터

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

l,r = 0,1
result = sys.maxsize
while l < n:
    d = arr[r]-arr[l]
    if d == m:
        result = m
        break
    if d < m:
        r += 1
        if r == n: break
    else:
        l += 1
        result = min(result,d)

print(result)