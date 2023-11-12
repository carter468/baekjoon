# 빨강~ 빨강~ 파랑! 파랑! 달콤한 솜사탕!
# Gold 5, binary search

import sys,bisect
input = sys.stdin.readline

n,q = map(int,input().split())
R,B = [],[]
for i,a in enumerate(input()):
    if a == 'R': R.append(i)
    if a == 'B': B.append(i)
    
for _ in range(q):
    l,r = map(int,input().split())
    a = bisect.bisect_left(R,l)
    b = bisect.bisect_left(B,r+1)-1
    if a <= len(R)-2 and b >= 1 and R[a+1] < B[b-1]:
        print(R[a],R[a+1],B[b-1],B[b])
    else:
        print(-1)