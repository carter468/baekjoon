# Praca zdalna
# Gold 5, ternary search

import sys
input = sys.stdin.readline

def f(x):
    return sum([max(0,l-x,x-r) for l,r in arr])

arr = [tuple(map(int,input().split())) for _ in range(int(input()))]

lo,hi = 0,10**9
while lo+3 < hi:
    m1 = (lo*2+hi)//3
    m2 = (lo+hi*2)//3
    if f(m1) < f(m2): hi = m2
    else: lo = m1

print(*min([(f(i),i) for i in range(lo,lo+3)])[::-1])