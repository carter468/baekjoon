# 개구리 점프
# Gold 3, sweeping, disjoint set

import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = sorted([list(map(int,input().split()))[:2]+[i] for i in range(n)])

result = list(range(n))
e,idx = arr[0][1:]
for x1,x2,i in arr:
    if e >= x1: result[i] = result[idx]
    else: idx = i
    e = max(e,x2)

for _ in range(q):
    a,b = map(int,input().split())
    if result[a-1] == result[b-1]: print(1)
    else: print(0)