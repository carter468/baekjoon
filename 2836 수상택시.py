# 수상 택시
# Gold 3, sweeping

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    if a > b: arr.append((b,a))

result = m
l,r = 0,0
for a,b in sorted(arr):
    if a > r:
        result += (r-l)*2
        l,r = a,b
    else:
        r = max(r,b)
print(result+(r-l)*2)