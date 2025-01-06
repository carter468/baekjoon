# 선형 회귀는 너무 쉬워 4
# Gold 2, ternary search

import sys
input = sys.stdin.readline
from decimal import *
getcontext().prec = 50

def f(a):
    return a**4*p+a**3*q+a**2*r+a*s+t

n,b = map(int,input().split())
p,q,r,s,t = 0,0,0,0,0
for _ in range(n):
    x,y = map(int,input().split())
    z = b-y
    p += x**4
    q += 4*x**3*z
    r += 6*x*x*z*z
    s += 4*x*z**3
    t += z**4

lo,hi = Decimal(-1_000_000_000), Decimal(1_000_000_000)
while hi-lo > 1e-7:
    m1,m2 = (lo*2+hi)/Decimal(3),(lo+hi*2)/Decimal(3)
    if f(m1) > f(m2): lo = m1
    else: hi = m2
print(hi)