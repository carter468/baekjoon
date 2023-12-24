# 케이크 자르기
# Gold 5, binary search

import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
arr = [int(input()) for _ in range(m)]+[l]

for _ in range(n):
    q = int(input())
    lo,hi = 0,l+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        count = 0
        prev = 0
        for s in arr:
            if s-prev >= mid:
                count += 1
                prev = s
        if count > q: lo = mid
        else: hi = mid
    print(lo)