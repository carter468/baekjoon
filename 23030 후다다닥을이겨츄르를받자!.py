# 후다다닥을 이겨 츄르를 받자!
# Gold 3, dijkstra

import sys,heapq
input = sys.stdin.readline

n = int(input())
arr = tuple(map(int,input().split()))
tf = [[False]*51 for _ in range(n+1)]
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    tf[a][b] = (c,d)
    tf[c][d] = (a,b)

for _ in range(int(input())):
    t,x1,y1,x2,y2 = map(int,input().split())
    dist = [[10**9]*51 for _ in range(n+1)]
    dist[x1][y1] = 0
    q = [(0,x1,y1)]
    while q:
        d,x,y = heapq.heappop(q)
        if d > dist[x][y]: continue
        for ny in (y+1),(y-1):
            if 0 < ny <= arr[x-1]:
                nd = d+1
                if nd < dist[x][ny]:
                    dist[x][ny] = nd
                    heapq.heappush(q,(nd,x,ny))
        if tf[x][y]:
            nx,ny = tf[x][y]
            nd = d+t
            if nd < dist[nx][ny]:
                dist[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))
    print(dist[x2][y2])