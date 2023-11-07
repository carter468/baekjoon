# 누가 이길까
# Gold 5, binary search

import bisect

N,M = map(int,input().split())
HI = tuple(map(int,input().split()))
ARC = sorted(map(int,input().split()))

w,d = 0,0
for p in HI:
    a = bisect.bisect_left(ARC,p)
    b = bisect.bisect_right(ARC,p)
    w += a
    d += b-a
    
print(w,N*M-w-d,d)