# 수돗물과 게 임
# Gold 2, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

dx = -1,0,1,0
dy = 0,-1,0,1

N,M,T = map(int,input().split())
grid = [input() for _ in range(N)]

dist = [[[INF]*4 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] not in '.TS':
            s,e,d = i,j,int(grid[i][j])

dist[s][e][d] = 0
q = [(0,s,e,d)]
while q:
    t,x,y,d = heapq.heappop(q)
    if t > dist[x][y][d]: continue

    nd = (d+1)%4
    nt = t+T
    if nt < dist[x][y][nd]:
        dist[x][y][nd] = nt
        heapq.heappush(q,(nt,x,y,nd))

    nt = t+1
    for k in (1,-1):
        k = (d+k)%4
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            nd = d
            if grid[nx][ny] == 'T':
                c = 0
                while True:
                    c += 1
                    nd = (nd+1)%4
                    nx += dx[nd]
                    ny += dy[nd]
                    if nx < 0 or nx == N or ny < 0 or ny == M or grid[nx][ny] != 'T' or c == 4:
                        break
                if c == 4: nx = -1
            if 0 <= nx < N and 0 <= ny < M and nt < dist[nx][ny][nd]:
                dist[nx][ny][nd] = nt
                heapq.heappush(q,(nt,nx,ny,nd))

result = INF
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'S':
            result = min(result,min(dist[i][j]))

print(result if result != INF else -1)