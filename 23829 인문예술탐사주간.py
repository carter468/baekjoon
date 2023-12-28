# 인문예술탐사주간
# Gold 4, binary search, prefix sum

import sys
input = sys.stdin.readline

n,q = map(int,input().split())
arr = sorted(map(int,input().split()))

psum = [arr[0]]
for i in range(n-1):
    psum.append(psum[-1]+arr[i+1])

for _ in range(q):
    x = int(input())
    lo,hi = -1,n
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] <= x: lo = mid
        else: hi = mid
    if lo == -1: print(psum[-1]-x*n)
    else: print(psum[-1]-x*n-(psum[lo]-x*hi)*2)