# Ax+Bsin(x)=C ②
# Gold 3, math, binary search

import math

A,B,C = map(int,input().split())
lo,hi = (C-B)/A,(C+B)/A
while lo+1e-10 < hi:
    mid = (lo+hi)/2
    if A*mid+B*math.sin(mid) < C: lo = mid
    else: hi = mid
print(hi)