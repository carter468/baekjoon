# 선형 회귀는 너무 쉬워 3
# Gold 3, binary search

import sys
input = sys.stdin.readline

def f(a):
    result = 0
    for x,y in arr:
        result += (y-a*x-b)**3
    return result

n,b = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

lo,hi = -10**9,10**9
while hi-lo >= 1e-7:
    mid = (lo+hi)/2
    if f(mid) < 0: hi = mid
    else: lo = mid
print(hi)