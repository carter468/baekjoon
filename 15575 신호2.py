# 신호 2
# Gold 1, DP

import sys
input = sys.stdin.readline

A = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

p = 10**9
while A:
    x,y1 = A.pop()
    y2 = y1
    while A and A[-1][0] == x:
        y2 = A.pop()[1]
    if p == 10**9:
        a = 0,y1
        b = 0,y2
    else:
        na = max(a[0]+((p-x)**2+(a[1]-y1)**2)**0.5,b[0]+((p-x)**2+(b[1]-y1)**2)**0.5)
        nb = max(a[0]+((p-x)**2+(a[1]-y2)**2)**0.5,b[0]+((p-x)**2+(b[1]-y2)**2)**0.5)
        a = na,y1
        b = nb,y2
    p = x
print(max(a[0],b[0]))