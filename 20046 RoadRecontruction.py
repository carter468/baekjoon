# Road Reconstruction
# Gold 4, dijkstra

import heapq
INF = 10**9

n,m = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(n)]

dist = [[INF]*m for _ in range(n)]
q = []
if grid[0][0] != -1:
    q.append((grid[0][0],0,0))
    dist[0][0] = grid[0][0]

while q:
    d,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if nx < 0 or nx == n or ny < 0 or ny == m or grid[nx][ny] == -1: continue
        nd = d+grid[nx][ny]
        if nd < dist[nx][ny]:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,nx,ny))

print(dist[-1][-1] if dist[-1][-1] != INF else -1)