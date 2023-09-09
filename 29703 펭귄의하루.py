# 펭귄의 하루
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': s = i,j
        elif grid[i][j] == 'H': h = i,j

q = deque([s])
visit = [[-1]*m for _ in range(n)]
visit[s[0]][s[1]] = 0
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 'D' and visit[nx][ny] == -1:
            visit[nx][ny] = visit[x][y]+1
            q.append((nx,ny))

result = sys.maxsize
q = deque([h])
visit1 = [[-1]*m for _ in range(n)]
visit1[h[0]][h[1]] = 0
while q:
    x,y = q.popleft()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 'D' and visit1[nx][ny] == -1:
            visit1[nx][ny] = visit1[x][y]+1
            q.append((nx,ny))
            if grid[nx][ny] == 'F' and visit[nx][ny] != -1:
                result = min(result,visit[nx][ny]+visit1[nx][ny])

print(result if result != sys.maxsize else -1)