# 소가 길을 건너는 이유 7
# Gold 2, dijkstra

import heapq

n,t = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

dist = [[[10**9]*3 for _ in range(n)] for _ in range(n)]
dist[0][0][0] = 0
q = [(0,0,0,0)]
while q:
    d,c,x,y = heapq.heappop(q)
    if d > dist[x][y][c]: continue
    c = (c+1)%3
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if nx < 0 or nx == n or ny < 0 or ny == n: continue
        nd = d+t
        if c == 0:
            nd += arr[nx][ny]
        if nd < dist[nx][ny][c]:
            dist[nx][ny][c] = nd
            heapq.heappush(q,(nd,c,nx,ny))
print(min(dist[-1][-1]))
