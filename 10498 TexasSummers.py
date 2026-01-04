# Texas Summers
# Gold 4, dijkstra, traceback

import sys,heapq
input = sys.stdin.readline

N = int(input())
A = [tuple(map(int,input().split())) for _ in range(N+2)]

dist = [sys.maxsize]*(N+1)+[0]
path = [None]*(N+2)
q = [(0,N+1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue

    x1,y1 = A[x]
    for nx in range(N+1):
        if x != nx:
            x2,y2 = A[nx]
            nd = d+(x1-x2)**2+(y1-y2)**2
            if nd < dist[nx]:
                dist[nx] = nd
                path[nx] = x
                heapq.heappush(q,(nd,nx))

x = N
result = []
while path[x] != N+1:
    x = path[x]
    result.append(x)

print(*result if result else '-',sep='\n')