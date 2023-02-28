# 게임
# Gold 5, 데이크스트라

import heapq
import sys
input = sys.stdin.readline
INF = 100000

def mark(n):
    for _ in range(int(input())):
        x1,y1,x2,y2 = map(int,input().split())
        x1,y1,x2,y2 = min(x1,x2),min(y1,y2),max(x1,x2),max(y1,y2)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] = n

grid = [[0]*501 for _ in range(501)]
mark(1)
mark(-1)

distance = [[INF]*501 for _ in range(501)]
distance[0][0] = 0
q = []
heapq.heappush(q,(0,(0,0)))
while q:
    dist, node = heapq.heappop(q)
    x,y = node
    if distance[x][y] < dist:
        continue
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny = x+dx,y+dy
        if nx<0 or nx==501 or ny<0 or ny==501 or grid[nx][ny]==-1:
            continue
        if distance[nx][ny]>dist+grid[nx][ny]:
            distance[nx][ny] = dist+grid[nx][ny]
            heapq.heappush(q,(distance[nx][ny],(nx,ny)))

print(distance[500][500] if distance[500][500]!=INF else -1)