# 바이러스 공격
# Gold 3, dijkstra

import heapq

n,m = map(int,input().split())
a,b,_,_ = map(int,input().split())
grid = [input() for _ in range(n)]

dist = [[2222]*m for _ in range(n)]
q = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            heapq.heappush(q,(0,i,j))
            dist[i][j] = 0

while q:
    d,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == '#': nd = d+b+1
            else: nd = d+1
            if nd < dist[nx][ny]:
                dist[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))

result = []
for i in range(n):
    for j in range(m):
        if dist[i][j] > a: result.append((i+1,j+1))
if result:
    for r in result: print(*r)
else: print(-1)