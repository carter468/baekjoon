# 성싶당 밀키트
# Gold 4, binary search

import sys
input = sys.stdin.readline

def check(x):
    g = 0
    temp = []
    for s,l,o in arr:
        c = s*max(1,x-l)
        if o == 1: temp.append(c)
        g += c
    temp.sort()
    for _ in range(min(K,len(temp))):
        g -= temp.pop()
    return g <= G

N,G,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

lo,hi = 0,10**10
while lo+1 < hi:
    mid = (lo+hi)>>1
    if check(mid): lo = mid
    else: hi = mid
print(lo)