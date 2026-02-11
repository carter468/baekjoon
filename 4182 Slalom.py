# Slalom
# Platinum 5, binary search

import sys
input = sys.stdin.readline

def check(x):
    l = gates[0][0]*x
    r = (gates[0][0]+W)*x
    for i in range(1,N):
        ll = gates[i][0]*x
        rr = (gates[i][0]+W)*x

        t = gates[i][1]-gates[i-1][1]
        l -= t*V
        r += t*V
        
        if l > rr or r < ll: return False
        l,r = max(l,ll),min(r,rr)
    return True

W,V,N = map(int,input().split())
gates = [tuple(map(int,input().split())) for _ in range(N)]
skis = [int(input()) for _ in range(int(input()))]

lo,hi = 1,10**6+1
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid

m = 0
for s in skis:
    if s <= lo: m = max(m,s)
print(m if m else 'IMPOSSIBLE')