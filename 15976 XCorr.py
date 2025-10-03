# XCorr
# Gold 3, prefix sum, binary search

import sys,bisect
input = sys.stdin.readline

X = [tuple(map(int,input().split())) for _ in range(int(input()))]
Y = [tuple(map(int,input().split())) for _ in range(int(input()))]
a,b = int(input()),int(input())

idxY = []
psumY = [0]
for idx,val in Y:
    idxY.append(idx)
    psumY.append(psumY[-1]+val)

result = 0
for idx,val in X:
    l = bisect.bisect_left(idxY,idx+a)
    r = bisect.bisect_right(idxY,idx+b)
    result += (psumY[r]-psumY[l])*val
print(result)