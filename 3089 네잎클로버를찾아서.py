# 네잎 클로버를 찾아서
# Gold 2, binary search

from bisect import bisect_left as bl,bisect_right as br
from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
X,Y = defaultdict(list),defaultdict(list)
for _ in range(n):
    x,y = map(int,input().split())
    X[x].append(y)
    Y[y].append(x)
for x in X: X[x].sort()
for y in Y: Y[y].sort()

x,y = 0,0
for d in input():
    if d == 'U':
        y = X[x][br(X[x],y)]
    elif d == 'D':
        y = X[x][bl(X[x],y)-1]
    elif d == 'R':
        x = Y[y][br(Y[y],x)]
    elif d == 'L':
        x = Y[y][bl(Y[y],x)-1]
print(x,y)