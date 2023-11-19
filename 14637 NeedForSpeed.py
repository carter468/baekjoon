# Need for Speed
# Gold 5, binary search

import sys
input = sys.stdin.readline

n,t = map(int,input().split())
distance,speed = [],[]
for _ in range(n):
    d,s = map(int,input().split())
    distance.append(d)
    speed.append(s)

lo = -min(speed)
hi = 10**9
while lo+10**-6 < hi:
    mid = (lo+hi)/2
    result = sum(distance[i]/(speed[i]+mid) for i in range(n))
    if result > t: lo = mid
    else: hi = mid
print(mid)