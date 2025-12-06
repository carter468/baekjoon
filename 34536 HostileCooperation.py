# Hostile Cooperation
# Platinum 5, game theory, binary search

import bisect

N,K = map(int,input().split())
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))
C = sorted(map(int,input().split()))

c1,c2 = C[0],C[-1]
k = K-(c1+c2)/2

m = 10**10
x = 0
for a in A:
    i = bisect.bisect_right(B,k-a)
    for j in (i,i-1):
        if j != N:
            b = B[j]
            d = abs(k-(a+b))
            if  d < m:
                m = d
                x = a+b

print(max(abs(K-(x+c1)),abs(K-(x+c2))))