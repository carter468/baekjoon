# 입국심사
# Gold 5, binary search

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]

lo,hi = 0,10**18
while lo+1 < hi:
    mid = (lo+hi)//2
    count = 0
    for a in arr:
        count += mid//a
    if count >= m: hi = mid
    else: lo = mid
print(hi)