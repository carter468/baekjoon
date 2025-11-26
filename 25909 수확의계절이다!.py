# 수확의 계절이다!
# Gold 2, binary search

import sys
input = sys.stdin.readline
D = {'E':(1,0),'W':(-1,0),'N':(0,1),'S':(0,-1)}

def check(k):
    count = 0
    seed = dict()
    x,y,t = 0,0,0
    for a,b in arr:
        dx,dy = D[a]
        for _ in range(b):
            x += dx
            y += dy
            t += 1
            if (x,y) in seed:
                if seed[(x,y)] <= t:
                    count += 1
                    seed[(x,y)] = t+k
            else:
                seed[(x,y)] = t+k
    return count >= K

N,K = map(int,input().split())
arr = []
for _ in range(N):
    a,b = input().split()
    arr.append((a,int(b)))

lo,hi = -1,10**7
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid

print(lo)