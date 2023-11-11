# 숫자탑과 쿼리
# Gold 5, binary search, math

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,d,x = map(int,input().split())
    lo,hi = 0,1414
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid*(2*a+(mid-1)*d)/2 < x: lo = mid
        else: hi = mid
    print(hi,x-lo*(2*a+(lo-1)*d)//2)