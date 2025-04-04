# gFiles (Large)
# Gold 5, math, case work

import sys
input = sys.stdin.readline
eps = 1e-8
mxinf = 1e18

def check(x):
    for p,k in arr:
        if p != 0 and k*100//x != p:
            return False
        if p == 100 and k != x:
            return False
    return True

for t in range(int(input())):
    arr = [tuple(map(int,input().split())) for _ in range(int(input()))]
    mn = 0
    mx = mxinf
    for p,k in arr:
        if p != 100:
            mn = max(mn,100*k/(p+1)-eps)
        mx = min(mx,100*k/p+eps if p != 0 else mxinf)

    ans = arr[-1][1] if arr[-1][0] == 100 else int(mx)
    if not check(ans):
        ans -= 1

    if not check(ans) or mn >= mx or check(ans+1) or check(ans-1):
        print(f"Case #{t+1}: -1")
    else:
        print(f"Case #{t+1}: {ans}")