# 파괴왕 뚱뽭
# Gold 1, dijkstra

import sys,heapq
input = sys.stdin.readline

n,m,k,t,q = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
tp = [[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    tp[x1-1][y1-1] = (x2-1,y2-1)

dist = [[[10**9]*m for _ in range(n)] for _ in range(t+1)]
dist[0][0][0] = 0
queue = [(0,0,0,0)]
while queue:
    d,x,y,c = heapq.heappop(queue)
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m:
            nd = d+arr[nx][ny]
            if nd < dist[c][nx][ny]:
                dist[c][nx][ny] = nd
                heapq.heappush(queue,(nd,nx,ny,c))
    if tp[x][y] and c < t:
        nx,ny = tp[x][y]
        if d < dist[c+1][nx][ny]:
            dist[c+1][nx][ny] = d
            heapq.heappush(queue,(d,nx,ny,c+1))

for _ in range(q):
    p,x,y = map(int,input().split())
    for i in range(t+1):
        if dist[i][x-1][y-1] <= p:
            print(1)
            break
    else: print(0)