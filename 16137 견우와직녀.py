# 견우와 직녀
# Gold 1, dijkstra

import heapq

N,M = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(N)]

dist = [[[99999]*2 for _ in range(N)] for _ in range(N)]
dist[0][0][0] = 0
q = [(0,0,0,0,0)]
while q:
    d,x,y,c,f = heapq.heappop(q)
    if d > dist[x][y][c]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] == 1:
                if d+1 < dist[nx][ny][c]:
                    dist[nx][ny][c] = d+1
                    heapq.heappush(q,(d+1,nx,ny,c,0))
            elif f == 0:
                if grid[nx][ny] > 1:
                    a = grid[nx][ny]
                    b = (a-d)%a
                    if b == 0: b = a
                    nd = d+b
                    if nd < dist[nx][ny][c]:
                        dist[nx][ny][c] = nd
                        heapq.heappush(q,(nd,nx,ny,c,1))
                elif c == 0:
                    b = (M-d)%M
                    if b == 0: b = M
                    nd = d+b
                    if nd < dist[nx][ny][1]:
                        dist[nx][ny][1] = nd
                        heapq.heappush(q,(nd,nx,ny,1,1))

print(min(dist[-1][-1]))