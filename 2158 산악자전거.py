# 산악자전거
# Gold 3, dijkstra

import heapq

v,r,c = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(r)]

q = [(0,v,0,0)]
dist = [[10**20]*c for _ in range(r)]
dist[0][0] = 0
while q:
    d,v,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue
    nd = d+1/v
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < r and 0 <= ny < c and nd < dist[nx][ny]:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,v*(2**(arr[x][y]-arr[nx][ny])),nx,ny))
print(dist[-1][-1])