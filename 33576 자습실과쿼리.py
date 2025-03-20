# 자습실과 쿼리
# Gold 5, prefix sum, two pointer

import sys
input = sys.stdin.readline

N,M,Q = map(int,input().split())
arr = [0]*(N+1)
for _ in range(M):
    w,d = map(int,input().split())
    arr[w] = d
for i in range(N):
    arr[i+1] += arr[i]

l,r = 0,N
for _ in range(Q):
    p = int(input())
    if p <= l: a = 0
    else: a = arr[p]-arr[l]
    if p >= r: b = 0
    else: b = arr[r]-arr[p]
    if a < b:
        result = a
        l = max(l,p)
    elif a > b:
        result = b
        r = min(r,p)
    else:
        if p-1 <= N-p:
            result = a
            l = max(l,p)
        else:
            result = b
            r = min(r,p)
    print(result)