# 네모난 순열 찾기 2
# Gold 5, ad hoc

import sys
input = sys.stdin.readline

N = int(input())
A = [tuple(map(int,input().split())) for _ in range(N)]

pos = dict()
for i in range(N):
    for j in range(N):
        pos[A[i][j]] = (i,j)

count = 0
minx,miny,maxx,maxy = N,N,0,0
for i in range(1,N*N+1):
    x,y = pos[i]
    minx,miny,maxx,maxy = min(minx,x),min(miny,y),max(maxx,x),max(maxy,y)
    if (maxx-minx+1)*(maxy-miny+1) == i: count += 1
print(count)