# 기숙사 소등
# Gold 2, ad hoc, binary search

import bisect

N,K = map(int,input().split())
A = sorted(map(int,input().split()))
arr = tuple(map(int,input().split()))

result = 0
c1,c2 = 0,0
for a in arr:
    if a == 0: 
        c1 += 1
    else:
        i = bisect.bisect_left(A,c1)
        if i < K and c1+c2 >= A[i]:
            c2 += 1
print(N-c1-c2)