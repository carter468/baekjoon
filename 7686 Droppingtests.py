# Dropping tests
# Platinum 5, binary search, greedy

import sys
input = sys.stdin.readline

def check(x):
    return sum(sorted([a-b*x/100 for a,b in zip(A,B)])[K:]) < 0

while True:
    N,K = map(int,input().split())
    if N == 0: break
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))

    lo,hi = 0,100
    for _ in range(22):
        mid = (lo+hi)/2
        if check(mid): hi = mid
        else: lo = mid
    print(round(hi))