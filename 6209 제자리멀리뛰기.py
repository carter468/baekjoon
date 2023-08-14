# 제자리 멀리뛰기
# Gold 3, binary search

import sys
input = sys.stdin.readline

d,n,m = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])+[d]

l,r = 0,d+1
while l <= r:
    mid,c,x = (l+r)//2,0,0
    for a in arr:
        if a-x < mid:
            c += 1
        else:
            x = a
    if c <= m:
        l = mid+1
    else:
        r = mid-1

print(r)