# Portals
# Platinum 3, BFS, dijkstra

from collections import deque
import sys,heapq
input = sys.stdin.readline

R,C = map(int,input().split())
grid = ['#'*(C+2)]
for _ in range(R):
    grid.append('#'+input().strip()+'#')
grid.append('#'*(C+2))
R,C = R+2,C+2

q = deque()
near = [[-1]*C for _ in range(R)]
graph = [[[] for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == '#':
            near[i][j] = 0
            q.append((i,j))
            for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                ni,nj = i+di,j+dj
                while 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#':
                    graph[ni][nj].append((i+di,j+dj))
                    ni += di
                    nj += dj
        elif grid[i][j] == 'S':
            sx,sy = i,j
        elif grid[i][j] == 'C':
            ex,ey = i,j
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < R and 0 <= ny < C and near[nx][ny] == -1:
            near[nx][ny] = near[x][y]+1
            q.append((nx,ny))

dist = [[10**9]*C for _ in range(R)]
dist[sx][sy] = 0
q = [(0,sx,sy)]
while q:
    d,x,y = heapq.heappop(q)
    if d > dist[x][y]: continue

    nd = d+1
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and nd < dist[nx][ny]:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,nx,ny))
    
    nd = d+near[x][y]
    for nx,ny in graph[x][y]:
        if nd < dist[nx][ny]:
            dist[nx][ny] = nd
            heapq.heappush(q,(nd,nx,ny))

x = dist[ex][ey]
print(x if x != 10**9 else -1)