# 무등산 등반
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())
x,y = map(int,input().split())
a,b,c = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(N)]

dist = [[INF]*M for _ in range(N)]
dist[x-1][y-1] = 0
q = [(0,x-1,y-1)]
while q:
    d,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if nx < 0 or nx == N or ny < 0 or ny == M: continue
        dif = grid[x][y]-grid[nx][ny]
        if abs(dif) > c: continue
        if dif > 0: nd = d+dif*b
        elif dif < 0: nd = d-dif*a
        else: nd = d+1
        if nd < dist[nx][ny]:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,nx,ny))

m = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] > m:
            m = grid[i][j]
            x,y = i,j

print(dist[x][y] if dist[x][y] != INF else -1)