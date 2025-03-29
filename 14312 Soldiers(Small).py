# Soldiers (Small)
# Gold 1, game theory, ad hoc

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]

    while arr:
        maxA,maxD = 0,0
        for a,d in arr:
            maxA = max(maxA,a)
            maxD = max(maxD,d)
        narr = []
        for a,d in arr:
            if (a,d) == (maxA,maxD): return 'YES'
            if a != maxA and d != maxD: narr.append((a,d))
        arr = narr
    return 'NO'

for t in range(int(input())):
    print(f'Case #{t+1}: {solve()}')