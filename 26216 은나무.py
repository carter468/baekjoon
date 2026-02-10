# 은나무
# Gold 2, LCA, math

import sys
input = sys.stdin.readline

def find_h(x):
    for i in range(H-1,-1,-1):
        if x%((K+1)**i) == 0: return i

def upward(x,h):
    y = (K+1)**(h+1)
    return x//y*y

K,H,Q = map(int,input().split())
MAX = (K+1)**H-1
for _ in range(Q):
    a,b = map(int,input().split())
    if max(a,b) > MAX:
        print(-1)
        continue

    if a == b:
        print(0)
        continue

    ha = find_h(a)
    hb = find_h(b)
    a = upward(a,ha)
    b = upward(b,hb)

    result = abs(ha-hb)+2
    if ha != hb:
        if ha > hb: a,b,ha,hb = b,a,hb,ha
        for i in range(hb-ha):
            a = upward(a,ha+1+i)
    
    while a != b:
        hb += 1
        a = upward(a,hb)
        b = upward(b,hb)
        result += 2
    print(result)