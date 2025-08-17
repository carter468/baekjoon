# 군인
# Platinum 5, fenwick tree, binary search

import sys
input = sys.stdin.readline

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i <= N:
        tree[i] += dif
        i += (i&-i)

N = int(input())
tree = [0]*(N+1)
for i,x in enumerate(map(int,input().split())):
    update(i+1,x)

for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        update(*q[1:])
    else:
        lo,hi = 0,N
        while lo+1 < hi:
            mid = (lo+hi)//2
            if prefix_sum(mid) >= q[1]: hi = mid
            else: lo = mid
        print(hi)