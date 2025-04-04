# 하늘에서 떨어지는 infinity개의 별
# Gold 3, number theory, binary search

import math

def check(x):
    return s0+g*x < M

s0,X,M,D,K = map(int,input().split())

g = math.gcd(X,M)
lo,hi = 0,10**18
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
m = s0+g*lo
if m == 0: print(0)
else: print((D-1)//(K//m))