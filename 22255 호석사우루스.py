# 호석사우루스
# Gold 2, dijkstra

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
sx,sy,ex,ey = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(n)]

distance = [[[INF]*3 for _ in range(m)] for _ in range(n)]
distance[sx-1][sy-1][1] = 0
q = []
heapq.heappush(q,(0,1,sx-1,sy-1))
while q:
    d,c,x,y = heapq.heappop(q)
    if distance[x][y][c] < d: continue
    
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if (c,dx) == (1,0) or (c,dy) == (2,0): continue
        nx,ny = x+dx,y+dy
        if nx < 0 or nx == n or ny < 0 or ny == m or grid[nx][ny] == -1: continue
        dist = grid[nx][ny]
        count = (c+1)%3
        if distance[nx][ny][count] > dist+d:
            distance[nx][ny][count] = dist+d
            heapq.heappush(q,(dist+d,count,nx,ny))
answer = min(distance[ex-1][ey-1])

print(answer if answer != INF else -1)