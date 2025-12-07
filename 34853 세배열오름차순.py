# 세 배열 오름차순
# Gold 3, binary search

import sys,bisect
input = sys.stdin.readline

def check(x):
    count = 0
    for i in (A,B,C):
        count += bisect.bisect_left(arr[i-1],x)
    return count < j

N,Q = map(int,input().split())
arr = []
for _ in range(N):
    _,*k = map(int,input().split())
    arr.append(sorted(k))

for _ in range(Q):
    A,B,C,j = map(int,input().split())
    lo,hi = 0,10**9+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): lo = mid
        else: hi = mid
    print(lo)