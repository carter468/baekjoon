# 미로 탈출
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
sx,sy = map(int,input().split())
ex,ey = map(int,input().split())
sx,sy,ex,ey = sx-1,sy-1,ex-1,ey-1
grid = [tuple(map(int,input().split())) for _ in range(n)]

q = deque([(sx,sy,1)])
visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]
visit[sx][sy][1] = 0
while q:
    x,y,z = q.popleft()
    if (x,y) == (ex,ey):
        print(visit[x][y][z])
        break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][z] == -1:
            if grid[nx][ny] == 0:
                q.append((nx,ny,z))
                visit[nx][ny][z] = visit[x][y][z]+1
            elif z == 1:
                q.append((nx,ny,0))
                visit[nx][ny][0] = visit[x][y][z]+1
else: print(-1)