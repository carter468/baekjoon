# 2^3은?
# Gold 5, math, ad hoc

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p,q,r = map(int,input().split())

    print((min(q,r)+p-1)%(10**9+7))