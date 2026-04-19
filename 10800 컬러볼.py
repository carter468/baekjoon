# 컬러볼
# Gold 2, prefix sum, binary search

import sys
from bisect import bisect_left as bl
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

a = []
b = [[] for _ in range(N+1)]
for c,s in arr:
    a.append(s)
    b[c].append(s)

a.sort()
asum = [0]
for x in a:
    asum.append(asum[-1]+x)

bsum = [0]
for i in range(1,N+1):
    b[i].sort()
    c = [0]
    for x in b[i]:
        c.append(c[-1]+x)
    bsum.append(c)

print(*[asum[bl(a,s)]-bsum[c][bl(b[c],s)] for c,s in arr],sep='\n')