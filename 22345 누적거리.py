# 누적 거리
# Gold 2, prefix sum, binary search

import sys,bisect
input = sys.stdin.readline

N,Q = map(int,input().split())
A = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:x[1])

X = [-10**10]
pa = [0]
pax = [0]
for a,x in A:
    X.append(x)
    pa.append(pa[-1]+a)
    pax.append(pax[-1]+a*x)

for _ in range(Q):
    q = int(input())
    i = bisect.bisect_right(X,q)
    print(pax[-1]-pa[-1]*q-2*(pax[i-1]-pa[i-1]*q))