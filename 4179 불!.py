# 불!
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

R,C = map(int,input().split())
grid = [input() for _ in range(R)]

fire = [[INF]*C for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'F': 
            q.append((i,j))
            fire[i][j] = 0
        elif grid[i][j] == 'J':
            sx,sy = i,j
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and fire[nx][ny] == INF:
            fire[nx][ny] = fire[x][y]+1
            q.append((nx,ny))

q = deque([(sx,sy)])
visited = [[INF]*C for _ in range(R)]
visited[sx][sy] = 0
while q:
    x,y = q.popleft()
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(visited[x][y]+1)
        break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and visited[nx][ny] == INF and visited[x][y]+1 < fire[nx][ny]:
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))
else: print('IMPOSSIBLE')