# 히스토그램에서 가장 큰 직사각형
# Platinum 5, divided and conquer

import sys
input = sys.stdin.readline

def solve(l,r):
    if l == r: return arr_h[l]

    mid = (l+r)//2
    area = max(solve(l,mid),solve(mid+1,r))

    ll,rr = mid,mid+1
    h = min(arr_h[ll],arr_h[rr])
    area = max(area,h*2,arr_h[ll],arr_h[rr])
    while (l < ll or rr < r):
        if (rr < r and (ll <= l or arr_h[ll-1] < arr_h[rr+1])):
            rr += 1
            h = min(h,arr_h[rr])
        else:
            ll -= 1
            h = min(h,arr_h[ll])
        area = max(area,h*(rr-ll+1))
    return area

while True:
    n,*arr_h = map(int,input().split())
    if n == 0: break
    print(solve(0,n-1))