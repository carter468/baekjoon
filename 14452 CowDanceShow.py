# Cow Dance Show
# Gold 4, binary search, prioirty queue

import sys,heapq
input = sys.stdin.readline

def check(x):
    q = []
    for i in range(x):
        heapq.heappush(q,arr[i])
    for i in range(x,n):
        heapq.heappush(q,heapq.heappop(q)+arr[i])
    return max(q) <= t

n,t = map(int,input().split())
arr = [int(input()) for _ in range(n)]

lo,hi = 0,n
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
