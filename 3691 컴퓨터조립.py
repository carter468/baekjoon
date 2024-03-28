# 컴퓨터 조립
# Gold 3, binary search

from collections import defaultdict
import sys
input = sys.stdin.readline

def check(x):
    price = 0
    for p in part:
        m = 10**6
        for a,b in part[p]:
            if b >= x: m = min(m,a)
        price += m
    return True if price <= B else False

for _ in range(int(input())):
    N,B = map(int,input().split())
    part = defaultdict(list)
    for _ in range(N):
        a,b,c,d = input().split()
        part[a].append((int(c),int(d)))
    lo,hi = 0,10**9+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): lo = mid
        else: hi = mid
    print(lo)