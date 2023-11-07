# 미로
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(input().strip()) for _ in range(n)]

hole = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            if i in (0,n-1) or j in (0,m-1):
                hole.append((i,j))
            grid[i][j] = '@'

i,j = hole[0]
visited = [[0]*m for _ in range(n)]
visited[i][j] = 1
q = deque([(i,j)])
while q:
    x,y = q.popleft()
    if (x,y) == hole[1]: break
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and grid[nx][ny] == '@':
            visited[nx][ny] = visited[x][y]+1
            q.append((nx,ny))

while (x,y) != hole[0]:
    grid[x][y] = '.'
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == visited[x][y]-1:
            x,y = nx,ny
            break
grid[x][y] = '.'

for g in grid:
    print(''.join(g))